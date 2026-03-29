import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ConcertReader {

    public static void main(String[] args) {
        int numBands;
        if (args.length > 0) {
            numBands = Integer.parseInt(args[0]);
            if (numBands < 1) {
                System.out.println("Invalid argument, must be > 0.");
                return;
            }
        } else {
            numBands = 10;
        }
        
        Map<String, Integer> bandOccurrences = countBands();
        int totalConcerts = getTotalConcerts(bandOccurrences);
        System.out.println("Total number of concerts: " + totalConcerts);

        int totalBands = getTotalBands(bandOccurrences);
        System.out.println("Total number of unique bands: " + totalBands);

        List<Map.Entry<String, Integer>> topXBands = getTopXBands(bandOccurrences, numBands);

        System.out.println("\nTop " + numBands + " Most Viewed Bands:");
        for (int i = 0; i < Math.min(numBands, topXBands.size()); i++) {
            Map.Entry<String, Integer> entry = topXBands.get(i);
            System.out.println(entry.getKey() + " - " + entry.getValue() + " times seen");
        }
    }

    public static Map<String, Integer> countBands() {
        String filename = "concerts_text.txt";
        Map<String, Integer> bandOccurrences = new HashMap<>();
        Set<String> uniqueBands = new HashSet<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] bands = line.split("\\|");
                for (String band : bands) {
                    String bandName = band.trim();
                    int occurrences = getOccurrences(bandName);
                    bandName = stripOccurrences(bandName);
                    bandOccurrences.put(bandName, bandOccurrences.getOrDefault(bandName, 0) + occurrences);
                    uniqueBands.add(bandName);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		
        return bandOccurrences;
    }

    private static int getOccurrences(String band) {
        int occurrences = 1;
        Pattern pattern = Pattern.compile("\\((\\d+)x\\)");
        Matcher matcher = pattern.matcher(band);
        if (matcher.find()) {
            occurrences = Integer.parseInt(matcher.group(1));
        }
        return occurrences;
    }

    private static String stripOccurrences(String band) {
        return band.replaceAll("\\(\\d+x\\)", "").trim();
    }

    public static List<Map.Entry<String, Integer>> getTopXBands(Map<String, Integer> bandOccurrences, int numBands) {
        List<Map.Entry<String, Integer>> sortedBands = new ArrayList<>(bandOccurrences.entrySet());
        sortedBands.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        return sortedBands.subList(0, Math.min(numBands, sortedBands.size()));
    }

    private static int getTotalConcerts(Map<String, Integer> bandOccurrences) {
        int total = 0;
        for (int value : bandOccurrences.values()) {
            total += value;
        }
        return total;
    }

    private static int getTotalBands(Map<String, Integer> bandOccurrences) {
        return bandOccurrences.size();
    }
}
