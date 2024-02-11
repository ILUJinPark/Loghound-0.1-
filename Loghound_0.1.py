
import re

# Define a path to your log file
log_file_path = "path/to/your/logfile.log"

# A dictionary to hold count of failed login attempts by IP address
failed_login_attempts = {}

# Regular expression to match a pattern of failed login attempt
# This pattern might need to be adjusted depending on the log file's format
failed_login_pattern = re.compile(r'Failed login from (?P<ip_address>\d+\.\d+\.\d+\.\d+)')

# Open and read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        # Search for patterns of failed logins in each line
        match = failed_login_pattern.search(line)
        if match:
            ip_address = match.group('ip_address')
            # Count the occurrences of failed logins from each IP address
            if ip_address in failed_login_attempts:
                failed_login_attempts[ip_address] += 1
            else:
                failed_login_attempts[ip_address] = 1

# Display the results
for ip, count in failed_login_attempts.items():
    print(f"IP Address {ip} had {count} failed login attempts.")

# This is a very basic example. Real log analysis might require more complex pattern matching,
# handling different log formats, and identifying various types of suspicious activities.
