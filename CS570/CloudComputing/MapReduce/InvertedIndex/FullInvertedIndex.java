import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FullInvertedIndex {

    public static class TokenizerMapper extends Mapper<Object, Text, Text, Text> {
        private Text word = new Text();
        private Text docId = new Text();

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String fileName = ((FileSplit) context.getInputSplit()).getPath().getName();
            String[] words = value.toString().split("\\s+");

            for (int i = 0; i < words.length; i++) {
                String str = words[i];
                word.set(str);
                docId.set(fileName + "@" + i);
                context.write(word, docId);
            }
        }
    }

    public static class IntSumReducer extends Reducer<Text, Text, Text, Text> {
        private Text result = new Text();

        public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            Map<String, List<Integer>> fileIndices = new HashMap<>();
            for (Text val : values) {
                String[] docAndIndex = val.toString().split("@");
                String doc = docAndIndex[0];
                Integer index = Integer.parseInt(docAndIndex[1]);
                fileIndices.computeIfAbsent(doc, k -> new ArrayList<>()).add(index);
            }

            StringBuilder sb = new StringBuilder();
            for (Map.Entry<String, List<Integer>> entry : fileIndices.entrySet()) {
                sb.append(entry.getKey()).append(":").append(entry.getValue()).append(" ");
            }

            result.set(sb.toString().trim());
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
        if (otherArgs.length < 2) {
            System.err.println("Usage: FullInvertedIndex <in> [<in>...] <out>");
            System.exit(2);
        }

        Job job = Job.getInstance(conf, "Full Inverted Index");
        job.setJarByClass(FullInvertedIndex.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        for (int i = 0; i < otherArgs.length - 1; ++i) {
            TextInputFormat.addInputPath(job, new Path(otherArgs[i]));
        }

        TextOutputFormat.setOutputPath(job, new Path(otherArgs[otherArgs.length - 1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}