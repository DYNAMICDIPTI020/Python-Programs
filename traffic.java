import java.util.Scanner;

public class traffic {
    
    // Enum to represent traffic light colors
    enum TrafficLight {
        RED, YELLOW, GREEN
    }
    
    // Method to determine action based on traffic light color
    public static String getTrafficAction(TrafficLight light) {
        switch (light) {
            case RED:
                return "STOP! Wait for the light to turn green.";
            case YELLOW:
                return "CAUTION! Prepare to stop if safe to do so.";
            case GREEN:
                return "GO! Proceed with caution.";
            default:
                return "Invalid traffic light color!";
        }
    }
    
    // Method to simulate traffic light sequence
    public static void simulateTrafficLight() {
        TrafficLight[] sequence = {TrafficLight.GREEN, TrafficLight.YELLOW, TrafficLight.RED};
        
        System.out.println("\n=== Traffic Light Simulation ===");
        for (int i = 0; i < sequence.length; i++) {
            System.out.println("Light " + (i + 1) + ": " + sequence[i] + " - " + getTrafficAction(sequence[i]));
            
            // Simulate time delay
            try {
                Thread.sleep(2000); // 2 seconds delay
            } catch (InterruptedException e) {
                System.out.println("Simulation interrupted");
            }
        }
    }
    
    // Method to get user input and provide traffic action
    public static void interactiveTrafficLight() {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("\n=== Interactive Traffic Light ===");
        System.out.println("Enter traffic light color:");
        System.out.println("1. RED");
        System.out.println("2. YELLOW");
        System.out.println("3. GREEN");
        System.out.print("Choose option (1-3): ");
        
        int choice = scanner.nextInt();
        TrafficLight light;
        
        switch (choice) {
            case 1:
                light = TrafficLight.RED;
                break;
            case 2:
                light = TrafficLight.YELLOW;
                break;
            case 3:
                light = TrafficLight.GREEN;
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }
        
        System.out.println("\nTraffic Light: " + light);
        System.out.println("Action: " + getTrafficAction(light));
        
        scanner.close();
    }
    
    public static void main(String[] args) {
        System.out.println("🚦 TRAFFIC LIGHT MANAGEMENT SYSTEM 🚦");
        System.out.println("=====================================");
        
        // Display all possible actions
        System.out.println("\nTraffic Light Actions:");
        for (TrafficLight light : TrafficLight.values()) {
            System.out.println(light + ": " + getTrafficAction(light));
        }
        
        // Run interactive mode
        interactiveTrafficLight();
        
        // Run simulation
        simulateTrafficLight();
        
        System.out.println("\n🚗 Drive safely! 🚗");
    }
}
