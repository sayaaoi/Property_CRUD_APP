from flask import request, url_for, render_template, flash, redirect
from sqlalchemy import func, text
from app import app, db, ma
from app.models import Property, PropertySchema
from app.forms import PropertyFrom

# Add a property & Update a property & Get all properties
@app.route('/', methods=['GET','POST'])
def get_properties(): 
    all_properties = Property.query.all()
    num = db.session.query(Property).count()
    total_mv = db.session.query(func.sum(Property.MarketValue))
    total_cost = db.session.query(func.sum(Property.Cost))
    pl_result = db.session.query(func.sum(Property.MarketValue - Property.Cost))

    form = PropertyFrom()
    if request.method == 'POST':
        if form.PropertyID.data:
            current_property = Property.query.get(form.PropertyID.data)
            current_property.PropertyName = form.PropertyName.data
            current_property.City = form.City.data
            current_property.MarketValue = form.MarketValue.data
            current_property.Cost = form.Cost.data
            db.session.commit()
            flash('Update a property successfully', 'success')
        else:
            new_property = Property(PropertyName=form.PropertyName.data, 
                                    City=form.City.data, MarketValue=form.MarketValue.data, 
                                    Cost=form.Cost.data)
            db.session.add(new_property)
            db.session.commit()
            flash('Add a property successfully', 'success')
        return redirect(url_for('get_properties'))
    
    return render_template('properties.html', all_properties=all_properties, num=num, 
                            total_mv=total_mv, total_cost=total_cost, pl_result=pl_result,
                            form=form)

# Delete a property
@app.route('/delete/<string:p_id>', methods=['GET'])
def delete(p_id):
    property = Property.query.get(p_id)
    db.session.delete(property)
    db.session.commit()
    flash('Delete a property successfully', 'success')
    return redirect(url_for('get_properties'))


