import time
import os
from datetime import datetime

class TrafficLight:
    def __init__(self):
        self.states = ["RED", "YELLOW", "GREEN"]
        self.current_state = 0  # Start with RED
        self.timings = {
            "RED": 10,      # Red light for 10 seconds
            "YELLOW": 3,    # Yellow light for 3 seconds  
            "GREEN": 15     # Green light for 15 seconds
        }
        self.running = True
        
    def get_current_light(self):
        return self.states[self.current_state]
    
    def get_current_timing(self):
        return self.timings[self.get_current_light()]
    
    def next_state(self):
        self.current_state = (self.current_state + 1) % len(self.states)
    
    def display_traffic_light(self):
        """Display the traffic light with colors"""
        current_light = self.get_current_light()
        
        # Clear screen (works on Windows)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 40)
        print("        TRAFFIC LIGHT SYSTEM")
        print("=" * 40)
        print(f"Current Time: {datetime.now().strftime('%H:%M:%S')}")
        print()
        
        # Display traffic light
        print("    ┌─────────────┐")
        
        # Red light
        if current_light == "RED":
            print("    │     ●       │  <- RED (STOP)")
        else:
            print("    │     ○       │")
            
        # Yellow light  
        if current_light == "YELLOW":
            print("    │     ●       │  <- YELLOW (CAUTION)")
        else:
            print("    │     ○       │")
            
        # Green light
        if current_light == "GREEN":
            print("    │     ●       │  <- GREEN (GO)")
        else:
            print("    │     ○       │")
            
        print("    └─────────────┘")
        print()
        
        # Display status
        print(f"Current State: {current_light}")
        print(f"Duration: {self.get_current_timing()} seconds")
        
        # Display instructions based on light
        if current_light == "RED":
            print("🛑 STOP! Do not cross the intersection.")
        elif current_light == "YELLOW":
            print("⚠️  CAUTION! Prepare to stop.")
        elif current_light == "GREEN":
            print("✅ GO! Safe to proceed.")
            
        print("\nPress Ctrl+C to stop the simulation")
        print("=" * 40)

class TrafficSimulation:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.total_cycles = 0
        
    def run_simulation(self):
        """Run the traffic light simulation"""
        print("Starting Traffic Light Simulation...")
        print("Press Ctrl+C at any time to stop\n")
        time.sleep(2)
        
        try:
            while self.traffic_light.running:
                # Display current state
                self.traffic_light.display_traffic_light()
                
                # Wait for the specified duration
                current_timing = self.traffic_light.get_current_timing()
                
                # Countdown timer
                for remaining in range(current_timing, 0, -1):
                    print(f"\rTime remaining: {remaining} seconds", end="", flush=True)
                    time.sleep(1)
                
                # Move to next state
                self.traffic_light.next_state()
                
                # Increment cycle counter when we complete a full cycle (back to RED)
                if self.traffic_light.get_current_light() == "RED":
                    self.total_cycles += 1
                    
        except KeyboardInterrupt:
            self.stop_simulation()
    
    def stop_simulation(self):
        """Stop the simulation and show statistics"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 40)
        print("    TRAFFIC SIMULATION STOPPED")
        print("=" * 40)
        print(f"Total complete cycles: {self.total_cycles}")
        print(f"Final state: {self.traffic_light.get_current_light()}")
        print(f"Simulation ended at: {datetime.now().strftime('%H:%M:%S')}")
        print("Thank you for using the Traffic Light Simulation!")
        print("=" * 40)

def show_menu():
    """Display the main menu"""
    print("=" * 40)
    print("    TRAFFIC LIGHT SIMULATION")
    print("=" * 40)
    print("1. Start Traffic Light Simulation")
    print("2. View Traffic Light Timings")
    print("3. Customize Timings")
    print("4. Exit")
    print("=" * 40)

def view_timings(traffic_light):
    """Display current traffic light timings"""
    print("\nCurrent Traffic Light Timings:")
    print("-" * 30)
    for state, timing in traffic_light.timings.items():
        print(f"{state:8}: {timing:2} seconds")
    print("-" * 30)

def customize_timings(traffic_light):
    """Allow user to customize traffic light timings"""
    print("\nCustomize Traffic Light Timings:")
    print("(Press Enter to keep current value)")
    
    for state in traffic_light.states:
        current_time = traffic_light.timings[state]
        while True:
            try:
                user_input = input(f"{state} light duration (current: {current_time}s): ")
                if user_input.strip() == "":
                    break
                new_time = int(user_input)
                if new_time > 0:
                    traffic_light.timings[state] = new_time
                    print(f"✅ {state} light set to {new_time} seconds")
                    break
                else:
                    print("❌ Please enter a positive number")
            except ValueError:
                print("❌ Please enter a valid number")

def main():
    """Main function to run the traffic program"""
    simulation = TrafficSimulation()
    
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                simulation.run_simulation()
            elif choice == "2":
                view_timings(simulation.traffic_light)
                input("\nPress Enter to continue...")
            elif choice == "3":
                customize_timings(simulation.traffic_light)
                input("\nPress Enter to continue...")
            elif choice == "4":
                print("\nThank you for using the Traffic Light Simulation!")
                print("Goodbye! 👋")
                break
            else:
                print("❌ Invalid choice. Please select 1-4.")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            time.sleep(2)
        
        # Clear screen before showing menu again
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()