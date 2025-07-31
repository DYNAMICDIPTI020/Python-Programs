import speech_recognition as sr
import pyttsx3
import time
import threading
import queue
import os
from datetime import datetime
import json

class AICallAnswerer:
    def __init__(self):
        """Initialize the AI Call Answerer with speech recognition and text-to-speech"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.microphone = sr.Microphone()
        self.call_queue = queue.Queue()
        self.is_answering = False
        self.call_log = []
        
        # Configure text-to-speech engine
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level
        
        # Get available voices and set a good one
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
    
    def speak(self, text):
        """Convert text to speech"""
        try:
            print(f"AI: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speech synthesis: {e}")
    
    def listen(self, timeout=5):
        """Listen for speech input and convert to text"""
        try:
            with self.microphone as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
                
            print("Processing speech...")
            text = self.recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return None
    
    def generate_response(self, user_message):
        """Generate AI response based on user input"""
        # Simple response logic - can be enhanced with more sophisticated AI
        user_message = user_message.lower()
        
        # Greeting responses
        if any(word in user_message for word in ['hello', 'hi', 'hey']):
            return "Hello! I'm your AI assistant. How can I help you today?"
        
        # Call-related responses
        elif any(word in user_message for word in ['call', 'phone', 'contact']):
            return "I understand you're calling. The person you're trying to reach is currently unavailable. Would you like to leave a message?"
        
        # Message-related responses
        elif any(word in user_message for word in ['message', 'leave', 'record']):
            return "I'll be happy to take your message. Please speak clearly after the beep."
        
        # Goodbye responses
        elif any(word in user_message for word in ['bye', 'goodbye', 'end', 'hang up']):
            return "Thank you for calling. Have a great day!"
        
        # Default response
        else:
            return "I'm sorry, I didn't quite catch that. Could you please repeat?"
    
    def answer_call(self):
        """Main function to answer and handle incoming calls"""
        self.is_answering = True
        call_start_time = datetime.now()
        
        # Initial greeting
        self.speak("Hello! You've reached the AI answering service. How may I assist you today?")
        
        conversation_log = []
        
        while self.is_answering:
            # Listen for user input
            user_input = self.listen(timeout=10)
            
            if user_input:
                # Log the conversation
                conversation_log.append({
                    'timestamp': datetime.now().isoformat(),
                    'speaker': 'caller',
                    'message': user_input
                })
                
                # Generate AI response
                ai_response = self.generate_response(user_input)
                
                # Log AI response
                conversation_log.append({
                    'timestamp': datetime.now().isoformat(),
                    'speaker': 'ai',
                    'message': ai_response
                })
                
                # Speak the response
                self.speak(ai_response)
                
                # Check if call should end
                if any(word in user_input for word in ['bye', 'goodbye', 'end', 'hang up']):
                    self.is_answering = False
                    break
                    
                # Check for silence (end call after 30 seconds of silence)
                time.sleep(2)
                
            else:
                # No speech detected, check if we should end the call
                print("No speech detected, continuing to listen...")
                time.sleep(1)
        
        # End call
        call_end_time = datetime.now()
        duration = (call_end_time - call_start_time).total_seconds()
        
        # Save call log
        call_record = {
            'call_id': len(self.call_log) + 1,
            'start_time': call_start_time.isoformat(),
            'end_time': call_end_time.isoformat(),
            'duration_seconds': duration,
            'conversation': conversation_log
        }
        
        self.call_log.append(call_record)
        self.save_call_log()
        
        print(f"Call ended. Duration: {duration:.1f} seconds")
        return call_record
    
    def save_call_log(self):
        """Save call logs to a JSON file"""
        try:
            with open('call_logs.json', 'w') as f:
                json.dump(self.call_log, f, indent=2)
            print("Call log saved successfully")
        except Exception as e:
            print(f"Error saving call log: {e}")
    
    def load_call_log(self):
        """Load call logs from JSON file"""
        try:
            if os.path.exists('call_logs.json'):
                with open('call_logs.json', 'r') as f:
                    self.call_log = json.load(f)
                print(f"Loaded {len(self.call_log)} previous call logs")
        except Exception as e:
            print(f"Error loading call log: {e}")
    
    def start_call_monitoring(self):
        """Start monitoring for incoming calls"""
        print("AI Call Answerer is now active and monitoring for calls...")
        print("Press Ctrl+C to stop the service")
        
        try:
            while True:
                # Simulate call detection (in real implementation, this would be actual call detection)
                print("\n" + "="*50)
                print("Simulating incoming call...")
                print("="*50)
                
                # Answer the call
                call_record = self.answer_call()
                
                print(f"\nCall Summary:")
                print(f"Duration: {call_record['duration_seconds']:.1f} seconds")
                print(f"Messages exchanged: {len(call_record['conversation'])}")
                
                # Ask if user wants to continue monitoring
                print("\nContinue monitoring for calls? (y/n): ", end="")
                response = input().lower()
                if response != 'y':
                    break
                    
        except KeyboardInterrupt:
            print("\nAI Call Answerer stopped by user")
        except Exception as e:
            print(f"Error in call monitoring: {e}")

def main():
    """Main function to run the AI Call Answerer"""
    print("AI Call Answerer System")
    print("=" * 30)
    
    # Initialize the AI call answerer
    ai_answerer = AICallAnswerer()
    
    # Load previous call logs
    ai_answerer.load_call_log()
    
    # Start call monitoring
    ai_answerer.start_call_monitoring()

if __name__ == "__main__":
    main()
