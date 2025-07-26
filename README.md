# 📦 AWS Cloud Cost Optimization — EBS Snapshot Cleanup Automation

> 🛠️ Built with Python, Boto3, and AWS Lambda  
> 🎯 Real-Time DevOps Use Case: Automated Cleanup of Stale EBS Snapshots  
> 🧠 Demonstrates Serverless Automation + Cloud Cost Efficiency  

---

Cloud storage costs often spiral due to **unused EBS snapshots** left behind from deleted EC2 volumes. This project offers a **real-time AWS Lambda-based solution** that intelligently identifies and deletes stale EBS snapshots — helping reduce unnecessary AWS charges and maintain DevOps hygiene.

## ✅ Key Highlights

- 💸 **Cloud Cost Optimization**: Automatically cleans up stale EBS snapshots.
- 🔁 **Serverless Automation**: Powered by AWS Lambda and Python (Boto3).
- 🔐 **Secure Access**: Uses minimal IAM permissions.
- 🧠 **Production-Ready Logic**: Real-world cloud scripting, ready to scale.

---

## 🧠 Problem Statement

In cloud environments, old EBS snapshots pile up and silently incur monthly storage costs. These are typically from EC2 instances that were terminated but their snapshots were never cleaned. Manual deletion is error-prone and inefficient. This Lambda function solves that.

### 🎯 Objectives

- List all EBS snapshots owned by the account
- Identify active EC2 instances (running or stopped)
- Find volume IDs attached to those instances
- Detect EBS snapshots not linked to any volume used by active instances
- Delete such stale snapshots

---

## ⚙️ Tools & Tech Used

- **Language**: Python 3.x
- **Cloud**: AWS Lambda, EC2, EBS
- **SDK**: Boto3
- **Security**: IAM Role-based Permissions
- **Monitoring**: CloudWatch (optional)

---

## 🔐 IAM Permissions Required

The Lambda function needs this minimal IAM policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeSnapshots",
        "ec2:DescribeVolumes",
        "ec2:DeleteSnapshot"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 🧪 How It Works (Architecture)

```plaintext
+------------------------+
| AWS Lambda (Python 3) |
+------------------------+
          |
          | Boto3 SDK
          v
+----------------------------+
| EC2 Describe Instances     |
| EC2 Describe Snapshots     |
| EC2 Describe Volumes       |
| EC2 Delete Snapshot        |
+----------------------------+
```

---

## 💻 Run This Project Locally (Test Before Deploying)

```bash
# Clone the repo
git clone https://github.com/chandukh2006/python-real-time-automations.git

# Navigate to the project folder
cd python-real-time-automations/python_boto3_aws_cost_optimization

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script (simulate Lambda locally)
python3 lambda_function.py
```

---

## ☁️ Deploy on AWS Lambda

1. Go to [AWS Lambda Console](https://console.aws.amazon.com/lambda/)
2. Create a new function → Choose "Author from scratch"
3. Upload the zipped `lambda_function.py`
4. Attach the IAM role with permissions listed above
5. (Optional) Add a trigger using **CloudWatch Events** to run periodically (e.g., weekly)

---

## 🖼️ Example Screenshots

Refer to the `screenshots/` folder in the repo for:

- Step-by-step Lambda deployment
- Sample output logs and cost savings


## 📂 Folder Structure

```
python_boto3_aws_cost_optimization/
├── lambda_function.py        # Main Python script
├── requirements.txt          # Boto3 dependency
└── screenshots/
    ├── steps/                # Setup screenshots
    └── result/               # Result screenshots
```

---

## 🌟 Why This Project Matters (To Recruiters)

| ✅ Area | 💬 What It Proves |
|--------|-------------------|
| Real-World Problem | Tackled AWS cost leakages proactively |
| Serverless Mindset | Built a Lambda-ready, automated cleanup |
| Python + Cloud | Combined scripting with infrastructure logic |
| Secure Practices | Implemented IAM least privilege model |
| DevOps Readiness | Reflects "automate everything" approach |

---

## 👨‍💻 Author

**Chandu K H**  
🎓 B.E. Computer Science (2023–2027), Navkis College of Engineering (VTU)  
⚙️ DevOps • AWS • Python • CI/CD • Automation  
📧 Email: khchandu291@gmail.com  
🔗 GitHub: [@chandukh2006](https://github.com/chandukh2006)

---

## ⭐ Bonus Tip for Reviewers

You can **test this entire automation without deploying** by running it locally with a configured AWS CLI session.

---

## 📌 Final Thoughts

> “DevOps isn’t just about CI/CD — it’s about writing clean, cost-efficient, and scalable infrastructure code.”

This project reflects:
- DevOps maturity  
- Real-world cloud automation  
- Problem-solving beyond basic scripting  

If you find this useful, feel free to ⭐️ star the repo and share with cloud enthusiasts!
