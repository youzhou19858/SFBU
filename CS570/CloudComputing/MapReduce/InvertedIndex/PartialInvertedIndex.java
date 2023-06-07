import java.io.*;
import java.util.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.Reducer.Context;
import org.apache.hadoop.util.*;

public class PartialInvertedIndex {
   public static class IndexMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text,Text> {
      public void map(LongWritable key, Text value, OutputCollector<Text,Text> output, Reporter reporter)throws IOException {
         FileSplit filesplit = (FileSplit) reporter.getInputSplit();
         String fileName = filesplit.getPath().getName();
         String line = value.toString();
         StringTokenizer tokenizer = new StringTokenizer(line);
         while (tokenizer.hasMoreTokens()) {
            String token = tokenizer.nextToken();
            output.collect(new Text(token.toLowerCase()), new Text(fileName));
         }
      }
   }
   public static class IndexReducer extends MapReduceBase implements Reducer<Text, Text,Text, DocSumWritable> {
      private HashMap<String, Integer> map;
      private void add (String tag) {
         Integer val;
         if (map.get(tag) != null) {
            val = map.get(tag);
            map.remove(tag);
         } else {
            val = 0;
         }
         map.put(tag, val+1);
      }
      public void reduce(Text key, Iterator<Text> value, OutputCollector<Text, DocSumWritable> output, Reporter reporter)throws IOException {
         map = new HashMap<String, Integer>();
         // HashSet<String> docId = new HashSet<String>();
         while(value.hasNext()) {
            add(value.next().toString());
         }
         output.collect(key, new DocSumWritable(map));
      }
   }
   
   public static void main(String[] args) throws IOException {
      JobConf conf = new JobConf(InvertedIndex.class);
      conf.setJobName("invertedIndexer");
      conf.setMapOutputKeyClass(Text.class);
      conf.setMapOutputValueClass(Text.class);
      conf.setOutputKeyClass(Text.class);
      conf.setOutputValueClass(DocSumWritable.class);
      conf.setMapperClass(IndexMapper.class);
      //conf.setCombinerClass(IndexReducer.class);
      conf.setReducerClass(IndexReducer.class);
      conf.setInputFormat(TextInputFormat.class);
      conf.setOutputFormat(TextOutputFormat.class);
      FileInputFormat.setInputPaths(conf, new Path (args[0]));
      FileOutputFormat.setOutputPath(conf, new Path (args[1]));
      JobClient.runJob(conf);
   }
}