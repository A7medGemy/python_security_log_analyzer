success = 0
fail = 0
ips = {}

with open("logs.txt", "r") as logs:
    for line in logs:

        if "LOGIN SUCCESS" in line:
            success += 1
        if "LOGIN FAILED" in line:
            fail += 1
            ip = line.split()[0]
            if ip in ips:
                ips[ip] += 1
            else:
                ips[ip] = 1
with open("report.txt", "w") as report:
    report.write(f"Security Log Analysis Report \n{'-' * 50}\n{'-' * 50}\n")

    report.write(f"Successful logins: {success} \nfailed logins: {fail}\n")

    if ips:
        most_suspicious_ip = max(ips, key=ips.get)
        report.write(f"Most suspicious ip: {most_suspicious_ip}\nFailed attempts: {ips[most_suspicious_ip]}")
    else:
        report.write("No failed login attempts detected ")
