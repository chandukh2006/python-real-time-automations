# 📦 AWS Cloud Cost Optimization — EBS Snapshot Cleanup Automation

> 🛠️ Built with Python, Boto3, and AWS Lambda  
> 🎯 Real-Time DevOps Use Case: Automated Cleanup of Stale EBS Snapshots  
> 🧠 Demonstrates Serverless Automation + Cost Efficiency

---

## 🚀 Project Overview

Cloud storage costs often spiral due to **unused EBS snapshots** left over from past operations. This project delivers a **real-time AWS Lambda-based automation** that programmatically **identifies and deletes stale EBS snapshots** no longer associated with active EC2 instances.

🎯 **Business Impact**:  
✅ Reduce AWS billing by eliminating storage waste  
✅ Maintain a clean and optimized cloud infrastructure  
✅ Enforce DevOps hygiene with automated cleanup

---

## 🧠 Problem Statement

> “Cloud cost optimization is not a feature — it’s a discipline.”

In large-scale AWS environments, **snapshots of terminated or unused EC2 volumes** linger, incurring unnecessary costs. Manual cleanup is error-prone and inefficient.

### 🔍 Goals:
- Identify all **EBS snapshots** owned by the account
- Determine if their associated **volumes** are linked to **running or stopped EC2 instances**
- **Delete stale snapshots** in a safe, automated way

---

## 🧪 Solution Architecture

```plaintext
+------------------------+
| AWS Lambda (Python 3) |
+------------------------+
          |
          | Boto3
          v
+------------------------+
| EC2 Describe Instances |
| EC2 Describe Snapshots |
| EC2 Describe Volumes   |
| EC2 Delete Snapshot    |
+------------------------+
