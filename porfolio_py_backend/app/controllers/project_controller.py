from flask import jsonify, request
from app import db
from app.models import Project, Tag

def get_projects():
  projects = Project.query.all()
  return jsonify([project.to_dict() for project in projects])


def create_project():
  data = request.get_json()
  
  project = Project(
      title=data['title'],
      description=data.get('description', ''),
      image=data.get('image', ''),
      date=data.get('date', ''),
      link=data.get('link', '')
  )
  
  for tag_name in data.get('tags', []):
      tag = Tag.query.filter_by(name=tag_name).first()
      if not tag:
          tag = Tag(name=tag_name)
          db.session.add(tag)
      project.tags.append(tag)
  
  db.session.add(project)
  db.session.commit()
  return jsonify(project.to_dict()), 201

































def get_project(id):
  project = Project.query.get_or_404(id)
  return jsonify(project.to_dict())





def update_project(id):
  project = Project.query.get_or_404(id)
  data = request.get_json()
  
  project.title = data.get('title', project.title)
  project.description = data.get('description', project.description)
  project.image = data.get('image', project.image)
  project.date = data.get('date', project.date)
  project.link = data.get('link', project.link)
  
  # Update tags
  if 'tags' in data:
      project.tags.clear()
      for tag_name in data['tags']:
          tag = Tag.query.filter_by(name=tag_name).first()
          if not tag:
              tag = Tag(name=tag_name)
              db.session.add(tag)
          project.tags.append(tag)
  
  db.session.commit()
  return jsonify(project.to_dict())

def delete_project(id):
  project = Project.query.get_or_404(id)
  db.session.delete(project)
  db.session.commit()
  return '', 204