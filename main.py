from send_email import send_transcription_email

# Step 1: This is the transcribed text (use your Whisper output)
transcribed_text = "This is what was spoken during the meeting..."

# Step 2: Email details
subject = "Meeting Notes"
sender_email = "akashsaravanasingh3@gmail.com"
app_password = "Akashabi@3"  # App password from Gmail
recipient_emails = ["dharun.meark@gmail.com", "kichukishore1504@gmail.com"]

# Step 3: Send the email
send_transcription_email(transcribed_text, subject, sender_email, app_password, recipient_emails)
