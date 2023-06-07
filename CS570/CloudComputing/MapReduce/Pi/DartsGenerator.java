import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Random;

public class DartsGenerator {
    private int n;
    private static final Random rand = new Random();

    public DartsGenerator(int radius, int n) {
        this.n = n;
    }

    public void generateDarts() {
        File file = new File("./input");
        try (PrintWriter pw = new PrintWriter(file)) {
            for (int i = 0; i < n; i++) {
                double x = rand.nextDouble() * 2 - 1;
                double y = rand.nextDouble() * 2 - 1;
                pw.println(x + "," + y);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Invalid arguments. Please provide R (radius) and N (number of pairs).");
            System.exit(1);
        }

        int radius = Integer.parseInt(args[0]);
        int n = Integer.parseInt(args[1]);
        
        DartsGenerator dartsGenerator = new DartsGenerator(radius, n);
        dartsGenerator.generateDarts();
    }
}
