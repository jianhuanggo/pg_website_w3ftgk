import sqlite3

loc_i = "assets/icons/"
loc_t = "assets/thumbnails/"

socials = [
    # social media and contact information
    {
        "platform": "email",
        "url": "mailto:my_user@gmail.com",
        "icon": loc_i + "email.png"
    },
    {
        "platform": "youtube",
        "url": "https://www.youtube.com/@my_user",
        "icon": loc_i + "youtube.png"
    },
    {
        "platform": "linkedin",
        "url": "https://linkedin.com/in/my_user",
        "icon": loc_i + "linkedin.png"
    },
    {
        "platform": "github",
        "url": "https://github.com/my_user",
        "icon": loc_i + "github.png"
    },
    {
        "platform": "x",
        "url": "https://x.com/my_user",
        "icon": loc_i + "x.png"
    }
]

projects = [
    # personal GitHub projects to showcase
    {
        "title": "Project Title 1",
        "description": "description of project 1",
        "url": "https://github.com/my_user/project1",
        "thumbnail": loc_t + "voice_chat.png"
    },
    {
        "title": "Project Title 2",
        "description": "description of project 2",
        "url": "https://github.com/my_user/project2",
        "thumbnail": loc_t + "stock_prediction.png"
    },
    {
        "title": "Project Title 3",
        "description": "description of project 3",
        "url": "https://github.com/my_user/project3",
        "thumbnail": loc_t + "recipe_picker.png"
    },
    {
        "title": "Project Title 4",
        "description": "description of project 4",
        "url": "https://github.com/my_user/project4",
        "thumbnail": loc_t + "image_gen.png"
    },
    {
        "title": "Project Title 5",
        "description": "description of project 5",
        "url": "https://github.com/my_user/project5",
        "thumbnail": loc_t + "dj_studio.png"
    },
]

skills = [
    # software and tools showcased in the protfolio
    {"name": "Python"},
    {"name": "HTML"},
    {"name": "CSS"},
    {"name": "Docker"},
]

profile = [
    {
        "name": "Pan",
        "title": "My job title",
        "bio": "Short description about me any my career goals.",
        "location": "my city, state/province"
    }
]

conn = sqlite3.connect('instance/portfolio.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS socials')
c.execute('DROP TABLE IF EXISTS projects')
c.execute('DROP TABLE IF EXISTS skills')
c.execute('DROP TABLE IF EXISTS profile')

c.execute('CREATE TABLE socials (id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, url TEXT, icon TEXT)')
c.execute('CREATE TABLE projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, url TEXT, thumbnail TEXT)')
c.execute('CREATE TABLE skills (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
c.execute('CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT, bio TEXT, location TEXT)')

c.executemany('INSERT INTO socials (platform, url, icon) VALUES (:platform, :url, :icon)', socials)
c.executemany('INSERT INTO projects (title, description, url, thumbnail) VALUES (:title, :description, :url, :thumbnail)', projects)
c.executemany('INSERT INTO skills (name) VALUES (:name)', skills)
c.executemany('INSERT INTO profile (name, title, bio, location) VALUES (:name, :title, :bio, :location)', profile)

conn.commit()
conn.close()

print("Database tables dropped and repopulated in instance/portfolio.db!")
