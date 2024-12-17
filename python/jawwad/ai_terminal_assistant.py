#!/usr/bin/env python3
import os
import subprocess
import sys
import google.generativeai as genai
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.syntax import Syntax

class AITerminalAssistant:
    def __init__(self, api_key):
        # Configure Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.console = Console()

    def suggest_command(self, context):
        """Suggest a command based on the user's context"""
        prompt = f"Suggest a Linux terminal command for: {context}. Provide only the command."
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating suggestion: {e}"

    def explain_command(self, command):
        """Explain a given command"""
        prompt = f"Explain the Linux terminal command '{command}' in detail, including its purpose and typical use cases."
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error explaining command: {e}"

    def diagnose_error(self, error_message):
        """Diagnose and suggest fixes for terminal errors"""
        prompt = f"Diagnose this Linux terminal error and suggest fixes: {error_message}"
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error diagnosing issue: {e}"
    def run_interactive_shell(self):
        """Run an interactive AI-powered terminal"""
        session = PromptSession()
        style = Style.from_dict({
            'prompt': '#ansigreen bold',
        })

        while True:
            try:
                # Custom prompt with AI indicator
                user_input = session.prompt('🤖 AI Terminal > ', style=style)

                # Special commands
                if user_input.lower() in ['exit', 'quit']:
                    break
                elif user_input.startswith('suggest:'):
                    suggestion = self.suggest_command(user_input[8:])
                    self.console.print(f"[bold green]Suggested Command:[/] {suggestion}")
                elif user_input.startswith('explain:'):
                    explanation = self.explain_command(user_input[8:])
                    self.console.print(f"[bold blue]Command Explanation:[/]\n{explanation}")
                else:
                    # General chat interaction
                    try:
                        prompt = f"You are a helpful AI assistant. Respond to the following: {user_input}"
                        response = self.model.generate_content(prompt)
                        self.console.print(f"[bold cyan]AI:[/] {response.text.strip()}")
                    
                    except Exception as e:
                        self.console.print(f"[bold red]Chat Error:[/] {e}")

            except KeyboardInterrupt:
                continue
            except EOFError:
                break

def main():
    # Get Gemini API key from environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable.")
        sys.exit(1)
    
    assistant = AITerminalAssistant(api_key)
    assistant.run_interactive_shell()

if __name__ == '__main__':
    main()
