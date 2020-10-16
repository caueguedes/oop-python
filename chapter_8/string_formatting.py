name = "Dusty"
activity = "writing"
formatted = f"Hello {name}, you are currently {activity}"
print(formatted)  # Hello Dusty, you are currently writing.


classname = "MyClass"
python_code = "print('hello world')"
template = f"""
public class {classname}
    public static void main(String[] args) {{
        System.out.println("{python_code}");
}}
"""

print(template)

# f-strings can contain python code

emails = ("a@example.com", "b@example.com")
message = {
    "subject": "You Have Mail!",
    "message": "Here's some mail for you!",
}

formatted_w_python = f"""
From: <{emails[0]}>
To: <{emails[1]}>
Subject: {message['subject']}
{message['message']}"""

print(formatted_w_python)