from app import db
from datetime import datetime

# Association table for Project and Tag (Many-to-Many)
project_tags = db.Table(
    "project_tags",
    db.Column("project_id", db.Integer, db.ForeignKey("project.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(500))
    date = db.Column(db.String(50))
    link = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with Tag model
    tags = db.relationship(
        "Tag", secondary=project_tags, backref=db.backref("projects", lazy=True)
    )

    def __repr__(self):
        return f"<Project {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "tags": [tag.name for tag in self.tags],
            "date": self.date,
            "link": self.link,
            "created_at": self.created_at.isoformat(),
        }


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Tag {self.name}>"
