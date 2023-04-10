from apps import db
from apps.authentication.models import User, Project, Team, Role
from flask_login import login_required, current_user


@login_required
def create_project(id, name, priority_id, product_id, creator_id, manager_id, create_date, status_update_date,
                   launch_date, end_date, visible, status_id, description, plan):
    new_project = Project(id=id, name=name, priority_id=priority_id, product_id=product_id, creator_id=creator_id,
                          manager_id=manager_id, create_date=create_date, status_update_date=status_update_date,
                          launch_date=launch_date, end_date=end_date, visible=visible, status_id=status_id,
                          description=description, plan=plan)
    db.session.add(new_project)
    db.session.commit()
    return new_project
