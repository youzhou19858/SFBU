import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

    public class PiEstimation {

        public static class TokenizerMapper
            extends Mapper<LongWritable, Text, Text, IntWritable> {

            private final static IntWritable one = new IntWritable(1);
            private final static IntWritable zero = new IntWritable(0);
            private Text word = new Text("Is in circle?");

            public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
                String[] xy = value.toString().split(",");
                double x = Double.parseDouble(xy[0]);
                double y = Double.parseDouble(xy[1]);
                if (x * x + y * y <= 1) {
                    context.write(word, one);
                } else {
                    context.write(word, zero);
                }
            }
    }

    public static class IntSumReducer
        extends Reducer<Text,IntWritable,Text,Text> {
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            double total = 0;
            double inCircle = 0;
            for (IntWritable val : values) {
                if (val.get() == 1) {
                    inCircle++;
                }
                total++;
            }
            double piEstimate = 4 * inCircle / total;
            context.write(key, new Text("Pi estimation: " + piEstimate));
        }
    }


    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Pi Estimation");
        job.setJarByClass(PiEstimation.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}

