from flask import Blueprint
from app.controllers.project_controller import (
    get_projects,
    get_project,
    create_project,
    update_project,
    delete_project,
)

project_routes = Blueprint("project_routes", __name__)


@project_routes.route("/projects", methods=["GET"])
def list_projects():
    return get_projects()




@project_routes.route("/projects", methods=["POST"])
def add_project():
    return create_project()

# @project_routes.route("/projects/<int:id>", methods=["GET"])
# def get_single_project(id):
#     return get_project(id)

# @project_routes.route("/projects/<int:id>", methods=["PUT"])
# def modify_project(id):
#     return update_project(id)


# @project_routes.route("/projects/<int:id>", methods=["DELETE"])
# def remove_project(id):
#     return delete_project(id)
