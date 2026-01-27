# RPG Inventory System

**Course:** INFO-H-303 - Databases
**University:** Université Libre de Bruxelles (ULB)
**Date:** March 2025

## 📜 Description

This project implements a complete **Inventory Management System for a Role-Playing Game (RPG)**. The goal is to efficiently structure a database to manage players, characters, items, quests, and battles.

The system relies on a relational database to handle core RPG mechanics, ensuring data integrity across various game elements. It supports features such as character evolution, inventory slot management, NPC interactions, and a combat system involving monsters and rewards.

## ✨ Features

* **Player & Character Management:** Handles user accounts and character stats (Strength, Agility, Mana, Level, etc.).
* **Inventory System:** Manages equipped items and inventory capacity based on character level.
* **Item Categorization:** distinct handling for **Weapons**, **Armors**, **Potions**, and **Artifacts**.
* **Quest & NPC Interaction:** Tracks quest status (names, difficulty, rewards) and NPC dialogues/trading.
* **Combat System:** Manages battles between characters and monsters, including loot drops and experience gain.
* **Class & Spell System:** Links characters to specific classes and class-specific spells.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

* **Python 3.x**
* **MySQL Server**

### Python Dependencies

Install the required Python libraries using `pip`:

```bash
pip install mysql-connector-python rich getkey

```

## 🚀 Installation & Database Setup

Follow these steps to set up the database and run the application.

### 1. Prepare the Shell Script

Navigate to the source directory and make the database script executable.

```bash
cd src
chmod +x db_script.sh

```

### 2. Configure and Run the Script

Open `db_script.sh` and update the password if necessary. Then, execute it:

```bash
./db_script.sh

```

### 3. Connect to MySQL

Connect to your MySQL instance.

* **Default User:** `pietro`
* **Default Database:** `rpgg`

```bash
mysql -u pietro -p rpgg

```

*When prompted for the password, enter:* `YildizMyGoat1!`

### 4. Load the Schema

Once inside the MySQL prompt, load the database schema. You can do this by navigating to the schema folder or pointing to the file path.

**Option A (Relative path from project root):**

```sql
SOURCE src/database/schema/all.sql;

```

**Option B (Navigate to folder first):**

```bash
cd src/database/schema
mysql -u pietro -p rpgg
SOURCE all.sql;

```

### 5. Import Initial Data

Populate the database with initial game data using the provided Python script.

```bash
cd ../../database  # Navigate to the /database folder
python3 importData.py data

```

## 🎮 Usage

To launch the RPGG application interface:

1. Navigate to the source directory:
```bash
cd src

```


2. Run the main application:
```bash
python3 rpgg.py

```



## 👥 Authors

* **Badi Budu Chris**
* **Lachhab Meryeme**
* **Narcisi Pietro**
* **Ngando Ngena Nicolas**
