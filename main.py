from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from google import genai

class ChatBotApp(App):
    def build(self):
        self.client = genai.Client(api_key="AIzaSyCJgmAcVsW6yRtZK-ZWVQGkVdTaBOOtylE")
        self.chat = self.client.chats.create(model="gemini-3.6-flash")
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.output = Label(text="🤖 AI Initialized!\n", halign="left", valign="top")
        self.output.bind(size=self.output.setter('text_size'))
        
        self.input = TextInput(hint_text="Type a message...", multiline=False, size_hint_y=None, height=100)
        btn = Button(text="Send", size_hint_y=None, height=100)
        btn.bind(on_press=self.send_msg)
        
        layout.add_widget(self.output)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

    def send_msg(self, instance):
        user_text = self.input.text
        if user_text:
            self.output.text += f"\nYou: {user_text}"
            self.input.text = ""
            try:
                response = self.chat.send_message(user_text)
                self.output.text += f"\nAI: {response.text}\n"
            except Exception as e:
                self.output.text += f"\n❌ Error: {e}\n"

if __name__ == '__main__':
    ChatBotApp().run()
