from flask import Flask,redirect,render_template,flash, request, session
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import AddPet


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "supersecretpasswordkey"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route ('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home_page.html', pets = pets)

@app.route('/add', methods=(['GET','POST']))
def add_new_pet():
    form = AddPet()
    
    if form.validate_on_submit():
        """This loop ensures that if nothing was entered in the form by the user,
        the data is set to None so that the SQL default doesn't get overwritten by an
        empty string"""
        
        for field in form:
            if field.data == '' or field.data=='-':
                field.data = None
        
        pet_name = form.pet_name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        photo_url = form.photo_url.data

        new_pet = Pet(name = pet_name, species = species,photo_url = photo_url, 
                      age = age, notes = notes, available = available)

        db.session.add(new_pet)
        db.session.commit()
        
        return redirect('/')

    else:
        return render_template('add_new_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=['POST','GET'])
def show_and_edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPet()

    
    if form.validate_on_submit():
       
     


        for field in form:
            if field.data == '' or field.data =='-':
                field.data = None
                print('*************************')
                print(field.name)
                print('*************************')
        
        pet.pet_name = form.pet_name.data 
        pet.species = form.species.data or pet.species
        pet.age = form.age.data
        pet.notes = form.notes.data or pet.notes
        pet.available = form.available.data 
        pet.photo_url = form.photo_url.data or pet.photo_url
        
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    return render_template('show_and_edit_pet.html', pet = pet, form = form)