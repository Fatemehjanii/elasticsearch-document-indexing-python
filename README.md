<div align="center">

# 🧠 Elasticsearch Learning Lab  
### by **Fatemeh** | Computer Engineer & DevOps Learner  

![Elastic Logo](https://upload.wikimedia.org/wikipedia/commons/f/f4/Elasticsearch_logo.svg)

---

</div>

## 🌍 Overview  
This repository is part of my **Elasticsearch learning journey** — focusing on mastering data indexing, searching, and scalability concepts.  
It includes theoretical explanations, Python scripts, and real queries tested on a local Elasticsearch cluster.

> 📘 Goal: Gain strong hands-on experience with Elasticsearch for DevOps, Data Engineering, and backend projects.

---

## 🧩 Topics Covered  

| # | Concept | Description |
|:-:|----------|--------------|
| 1 | Structured vs Unstructured Data | Understanding data organization and schema differences |
| 2 | Cluster | What an Elasticsearch cluster is and how it manages nodes |
| 3 | Scalability | Vertical vs Horizontal scaling concepts |
| 4 | Shards & Replicas | Internal data distribution and fault tolerance |
| 5 | Index & Templates | Creating indices, managing templates, and index states (Green / Yellow / Red) |
| 6 | Documents | Creating and inserting 100 structured documents using Python |
| 7 | Elasticsearch DSL | Query language and examples (match, filter, range, fuzzy, wildcard, etc.) |
| 8 | Aggregations | 5 types of aggregations and practical use cases |
| 9 | Reindex & Clone | Difference between reindexing and cloning |
| 10 | KQL & Kibana | Querying via Kibana dashboards and time-based visualizations |

---

## ⚙️ Project Structure

elasticsearch-learning-lab/
│
├── scripts/
│ └── bulk_insert_100.py # Python script for bulk document insertion
│
├── queries/
│ ├── 01_basic_match.json
│ ├── 02_filter_range.json
│ ├── ...
│ └── 100_complex_combined.json
│
├── templates/
│ └── index_template.json # Template for index mapping and validation
│
├── docker-compose.yml # Optional setup for running Elasticsearch & Kibana via Docker
│
└── README.md # You are here 😄

yaml
Copy code

---

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/elasticsearch-learning-lab.git
   cd elasticsearch-learning-lab
Install dependencies

bash
Copy code
pip install elasticsearch
Run local Elasticsearch

Option A: via Docker

bash
Copy code
docker-compose up -d
Option B: local installation on Windows

Insert sample documents

bash
Copy code
python scripts/bulk_insert_100.py
Run queries
Use the .json query files in queries/ to test different search patterns.

💡 Example Concepts Explained
📘 Structured vs Unstructured Data
Structured: Organized data with fixed schema — e.g., SQL tables, CSV files

Unstructured: Text, logs, JSON, images — no predefined schema

⚙️ What is a Cluster?
A cluster is a collection of one or more nodes (servers) that hold your data and provide search/index capabilities together.

📈 Scalability in Elasticsearch
Elasticsearch is horizontally scalable — you can add more nodes to distribute data and load.

Type	Description	Example
Not Scalable	Runs on one server only	Old monolithic apps
Vertical Scaling	Add more power to one machine	Upgrading CPU/RAM
Horizontal Scaling	Add more machines	Elasticsearch, Kubernetes

🔍 Elasticsearch DSL Highlights
Operator	Use Case
match	Text search in specific field
match_all	Returns all documents
filter	Filter based on exact conditions
must / should	Boolean logic inside queries
range	Numeric or date range
prefix	Partial match on beginning of string
wildcard	Search with * or ?
fuzzy	Match with spelling variations
aggregation	Statistical and grouped data insights

🧠 Extra Challenges
Write 100 queries ranging from basic match to complex combinations

Build a Kibana dashboard to visualize search results

Add a timestamp field (insert_time) for time-based queries

🛠️ Tools & Tech




👩‍💻 Author
Fatemeh
🧩 Computer Engineer | DevOps & AI Enthusiast
🌸 Member of Venomuse Rose Team
📍 Focus: Automation, Search Systems, and Data Engineering
🔗 GitHub Profile

⭐ Support
If you find this useful, give it a ⭐ on GitHub — it helps me grow and share more open-source learning projects!

<div align="center">
💬 "Search is not just finding — it’s understanding data."
— Fatemeh

