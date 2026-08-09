import os
import random
import string
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super_secret_key_for_session"

# Database Configuration
uri = os.environ.get('DATABASE_URL', 'sqlite:///complaints.db')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==========================================
# 1. DATABASE MODEL 
# ==========================================
class Complaint(db.Model):
    id = db.Column(db.String(20), primary_key=True) 
    student_name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(20), nullable=False) 
    department = db.Column(db.String(50), nullable=False) 
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default="Pending") 
    admin_response = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ==========================================
# 2. STUDENT ROUTING
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit_complaint():
    if request.method == 'POST':
        name = request.form['student_name']
        s_id = request.form['student_id']
        dept = request.form['department']
        desc = request.form['description']
        
        # Generate Unique Tracking ID (e.g., HSTU-A1B2C3)
        tracking_id = "HSTU-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
        new_complaint = Complaint(
            id=tracking_id, 
            student_name=name, 
            student_id=s_id, 
            department=dept, 
            description=desc
        )
        db.session.add(new_complaint)
        db.session.commit()
        
        flash(f"Complaint submitted successfully! Your Tracking ID is: {tracking_id}", "success")
        return redirect(url_for('track_complaint', tracking_id=tracking_id))
        
    return render_template('submit.html')

@app.route('/track', methods=['GET', 'POST'])
def track_complaint():
    complaint = None
    if request.method == 'POST':
        tracking_id = request.form['tracking_id'].strip()
        complaint = Complaint.query.get(tracking_id)
        if not complaint:
            flash("Invalid Tracking ID! Please provide a valid ID.", "danger")
            
    prefill_id = request.args.get('tracking_id', '')
    if prefill_id:
        complaint = Complaint.query.get(prefill_id)

    return render_template('track.html', complaint=complaint, prefill_id=prefill_id)

# ==========================================
# 3. ADMINISTRATOR ROUTING
# ==========================================
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid username or password!", "danger")
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        comp_id = request.form['complaint_id']
        complaint = Complaint.query.get(comp_id)
        if complaint:
            complaint.status = request.form['status']
            complaint.admin_response = request.form['admin_response']
            db.session.commit()
            flash(f"Complaint {comp_id} updated successfully.", "success")
            return redirect(url_for('admin_dashboard'))

    complaints = Complaint.query.order_by(Complaint.created_at.desc()).all()
    return render_template('admin_dashboard.html', complaints=complaints)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)