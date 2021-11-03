# HackTX2021_UT_JKK (UT Density Tracker)

## By Kashif, Jessie, and Kaylan

### Future Plans / Checklist

**During HackTX:**

- [x] Finish 'Building' Object (PYTHON) ~ Kaylan & Kashif
- [x] Create HTML Templates (CSS & HTML) ~ Jessie
- [x] Create a virtual environment & set up Flask ~ Kaylan
- [x] Set up the devpost page / chrome api ~ Kashif

**Post-HackTX:**

- [ ] Chrome API Integration (Google Sheets?)
- [ ] Store and display inputted user averages
- [ ] Finish connecting all HTML files through Flask
- [ ] Make an actual slider 

### What does it do?

The UT Density Tracker is intended to be an easy viewable web app that allows users to view the density of a given level of a given building. Through this they can better decide their plans regarding where to study and sit down. This is especially important in the current day, as COVID remains an incredibly infectious disease. As such, knowing what areas are more or less dense gives people an extra way to plan their day.

### How is Density Determined?

The density of a given building is determined by user inputted information. A user would go to the site and click on `X` level of `Y` building. From there they can view the current density of the building but they also have the choice to submit a value between `[0.1 - 10]` on how dense that part of the building is. Multiple user inputs are appended to a list, where they're all totaled and averaged. 

### Structure of our Code

The main way our `main.py` file is organized is through: 1) *A Building Object*, and 2) *Flask decorators tied to our HTML files*. The `Building` object has constructor variables for its name `Building.BLDG_NAME` and its number of levels `Building.NUMFLOORS`. The method `Building.makeBusynessList()` takes in said number of floors and creates a list of that length. `Building.addBusyNum()` and `Building.getAverage()` are in charge of adding a new value to a building at a given floor, and taking the mean/average of all values in a list.

### Technologies/Languages Used:
- Flask
- Python
- HTML
- CSS

### Post Project Notes:

##### (Kaylan):

While I wish we could've finished everything during the hackathon itself, the project gave me my first intro into Flask and how it could be configured into python. My two teammates were awesome people that I'm glad I got to meet. We probably should've done Javascript instead of Python just because it would've been easier to implement, but doing the latter let us all be more hands on with the project since we all knew. I thought the mentors would be a bit more involved with each of the teams and how they went about implementing features which might be my biggest gripe. All the documentation we had to read was pretty overwhelming, and it kind of felt like we were just dropped at sea. If I attend another hackathon I'll at least have a better idea of what I want to do and how I want to do it. Overall though, I'd say I learned a good deal.

