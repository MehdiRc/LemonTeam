# -*- coding: utf-8 -*-
"""
@author: Mehdi
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bar_R_by_age(data):
    under18 = np.array(data[data["age_-18"]==1])
    from18to24 = np.array(data[data["age_18-24"]==1])
    from25to34 = np.array(data[data["age_25-34"]==1])
    from35to44 = np.array(data[data["age_35-44"]==1])
    from45to49 = np.array(data[data["age_45-49"]==1])
    from50to55 = np.array(data[data["age_50-55"]==1])
    over56 = np.array(data[data["age_56+"]==1])
    
    avergaeUnder18=np.mean(under18[:,-1])
    avergaeFrom18to24 = np.mean(from18to24[:,-1])
    avergaeFrom25to34 = np.mean(from25to34[:,-1])
    avergaeFrom35to44 = np.mean(from35to44[:,-1])
    avergaeFrom45to49 = np.mean(from45to49[:,-1])
    avergaeFrom50to55 = np.mean(from50to55[:,-1])
    over56 = np.mean(over56[:,-1])
    
    averagesByAge=np.array([avergaeUnder18,avergaeFrom18to24,avergaeFrom25to34,avergaeFrom35to44,avergaeFrom45to49,avergaeFrom50to55,over56])
    
    plt.figure()
    plt.bar([0,18,25,35,45,50,55], averagesByAge, 3, color="g")
    plt.xlabel("$Age$")
    plt.ylabel("$Average Rating$") #$$ change apearence of font
    plt.title("$Average Ratings By Age Groups$")
    plt.savefig("Average Ratings By Age Groups.png") #to save the file

def bar_R_by_gender(data):
    males = np.array(data[data["gender_M"]==1])
    females = np.array(data[data["gender_F"]==1])
    
    averageMales=np.mean(males[:,-1])
    averageFemales=np.mean(females[:,-1])
    
    averageByGender=np.array([averageMales,averageFemales])
    averageByGender
    plt.figure()
    
    plt.bar(range(2),averageByGender , 0.5, color="br",align='center')
    plt.xticks(range(2), ["Males","Females"])
    
    plt.xlabel("$Gender$")
    plt.ylabel("$Average Rating$") #$$ change apearence of font
    plt.title("$Average Ratings By Gender$")
    plt.savefig("Average Ratings By Gender.png") #to save the file
    
def bar_R_by_jobs(data):
    job_other = np.array(data[data["job_other"]==1])
    job_academicOreducator = np.array(data[data["job_academic/educator"]==1])
    job_artist = np.array(data[data["job_artist"]==1])
    job_clericalOradmin = np.array(data[data["job_clerical/admin"]==1])
    job_collegeOrgrad_student = np.array(data[data["job_college/grad student"]==1])
    job_customer_service = np.array(data[data["job_customer service"]==1])
    job_doctorOrhealth_care = np.array(data[data["job_doctor/health care"]==1])
    job_executiveOrmanagerial = np.array(data[data["job_executive/managerial"]==1])
    job_farmer = np.array(data[data["job_farmer"]==1])
    job_homemaker = np.array(data[data["job_homemaker"]==1])
    job_K12_student = np.array(data[data["job_K-12 student"]==1])
    job_lawyer = np.array(data[data["job_lawyer"]==1])
    job_programmer = np.array(data[data["job_programmer"]==1])
    job_retired = np.array(data[data["job_retired"]==1])
    job_salesOrmarketing = np.array(data[data["job_sales/marketing"]==1])
    job_scientist = np.array(data[data["job_scientist"]==1])
    job_self_employed = np.array(data[data["job_self-employed"]==1])
    job_technicianOrengineer = np.array(data[data["job_technician/engineer"]==1])
    job_tradesmanOrcraftsman = np.array(data[data["job_tradesman/craftsman"]==1])
    job_unemployed = np.array(data[data["job_unemployed"]==1])
    job_writer = np.array(data[data["job_writer"]==1])
    
    
    avergaejob_other=np.mean(job_other[:,-1])
    avergaejob_academicOreducator=np.mean(job_academicOreducator[:,-1])
    avergaejob_artist=np.mean(job_artist[:,-1])
    avergaejob_clericalOradmin=np.mean(job_clericalOradmin[:,-1])
    avergaejob_collegeOrgrad_student=np.mean(job_collegeOrgrad_student[:,-1])
    avergaejob_customer_service=np.mean(job_customer_service[:,-1])
    avergaejob_doctorOrhealth_care=np.mean(job_doctorOrhealth_care[:,-1])
    avergaejob_executiveOrmanagerial=np.mean(job_executiveOrmanagerial[:,-1])
    avergaejob_farmer=np.mean(job_farmer[:,-1])
    avergaejob_homemaker=np.mean(job_homemaker[:,-1])
    avergaejob_K12_student=np.mean(job_K12_student[:,-1])
    avergaejob_lawyer=np.mean(job_lawyer[:,-1])
    avergaejob_programmer=np.mean(job_programmer[:,-1])
    avergaejob_retired=np.mean(job_retired[:,-1])
    avergaejob_salesOrmarketing=np.mean(job_salesOrmarketing[:,-1])
    avergaejob_scientist=np.mean(job_scientist[:,-1])
    avergaejob_self_employed=np.mean(job_self_employed[:,-1])
    avergaejob_technicianOrengineer=np.mean(job_technicianOrengineer[:,-1])
    avergaejob_tradesmanOrcraftsman=np.mean(job_tradesmanOrcraftsman[:,-1])
    avergaejob_unemployed=np.mean(job_unemployed[:,-1])
    avergaejob_writer=np.mean(job_writer[:,-1])
    
    
    
    averagesByJob=np.array([avergaejob_other,avergaejob_academicOreducator,avergaejob_artist,avergaejob_clericalOradmin,avergaejob_collegeOrgrad_student,avergaejob_customer_service,avergaejob_doctorOrhealth_care,avergaejob_executiveOrmanagerial,avergaejob_farmer,avergaejob_homemaker,avergaejob_K12_student,avergaejob_lawyer,avergaejob_programmer,avergaejob_retired,avergaejob_salesOrmarketing,avergaejob_scientist,avergaejob_self_employed,avergaejob_technicianOrengineer,avergaejob_tradesmanOrcraftsman,avergaejob_unemployed,avergaejob_writer])
    averagesByJob
    
    plt.figure()
    plt.bar(range(21),averagesByJob , 0.5, color="y",align='center',hatch="x")
    plt.xticks(range(21), ["Other","Academic/educator","Artist","Clerical/Admin","College/Grad Student","Customer Service","Doctor/Health Care","Executive/Managerial","Farmer","Homemaker","K12 Student","Lawyer","Programmer","Retired","Sales/Marketing","Scientist","Self Employed","Technician/Engineer","Tradesman/Craftsman","Unemployed","Writer"],rotation=90)
    
    plt.xlabel("$Jobs$")
    plt.ylabel("$Average Rating$") #$$ change apearence of font
    plt.title("$Average Ratings By Jobs$")
    plt.savefig("Average Ratings By Jobs.png") #to save the file
    


def bar_R_by_Genre(data):
    Action = np.array(data[data["movie_genre_Action"]==1])
    Adventure = np.array(data[data["movie_genre_Adventure"]==1])
    Animation = np.array(data[data["movie_genre_Animation"]==1])
    Childrens = np.array(data[data["movie_genre_Childrens"]==1])
    Comedy = np.array(data[data["movie_genre_Comedy"]==1])
    Crime = np.array(data[data["movie_genre_Crime"]==1])
    Documentary = np.array(data[data["movie_genre_Documentary"]==1])
    Drama = np.array(data[data["movie_genre_Drama"]==1])
    Fantasy = np.array(data[data["movie_genre_Fantasy"]==1])
    Film_Noir = np.array(data[data["movie_genre_Film-Noir"]==1])
    Horror = np.array(data[data["movie_genre_Horror"]==1])
    Musical = np.array(data[data["movie_genre_Musical"]==1])
    Mystery = np.array(data[data["movie_genre_Mystery"]==1])
    Romance = np.array(data[data["movie_genre_Romance"]==1])
    Sci_Fi = np.array(data[data["movie_genre_Sci-Fi"]==1])
    Thriller = np.array(data[data["movie_genre_Thriller"]==1])
    War = np.array(data[data["movie_genre_War"]==1])
    Western = np.array(data[data["movie_genre_Western"]==1])
    
    averageAction=np.mean(Action[:,-1])
    averageAdventure = np.mean(Adventure[:,-1])
    averageAnimation = np.mean(Animation[:,-1])
    averageChildrens = np.mean(Childrens[:,-1])
    averageComedy = np.mean(Comedy[:,-1])
    averageCrime = np.mean(Crime[:,-1])
    averageDocumentary = np.mean(Documentary[:,-1])
    averageDrama = np.mean(Drama[:,-1])
    averageFantasy = np.mean(Fantasy[:,-1])
    averageFilm_Noir = np.mean(Film_Noir[:,-1])
    averageHorror = np.mean(Horror[:,-1])
    averageMusical = np.mean(Musical[:,-1])
    averageMystery = np.mean(Mystery[:,-1])
    averageRomance = np.mean(Romance[:,-1])
    averageSci_Fi = np.mean(Sci_Fi[:,-1])
    averageThriller = np.mean(Thriller[:,-1])
    averageWar = np.mean(War[:,-1])
    averageWestern = np.mean(Western[:,-1])
    
    
    averagesByMovieGenre=np.array([averageAction, averageAdventure, averageAnimation, averageChildrens, averageComedy, averageCrime, averageDocumentary, averageDrama,averageFantasy,averageFilm_Noir,averageHorror,averageMusical,averageMystery,averageRomance,averageSci_Fi,averageThriller,averageWar,averageWestern])
    
    
    plt.figure()
    
    plt.bar(range(18),averagesByMovieGenre , 0.5, color="y")
    plt.xticks(range(18), ["Action","Adventure","Animation","Childrens","Comedy","Crime","Documentary","Drama","Fantasy","Film_Noir","Horror","Musical","Mystery","Romance","Sci_Fi","Thriller","War","Western"],rotation=70)
    
    plt.xlabel("$Genre$")
    plt.ylabel("$Average Rating$") #$$ change apearence of font
    plt.title("$Average Ratings By Movie Genre$")
    plt.savefig("Average Ratings By Movie Genre.png") #to save the file

def averageByAgeAndjob(data):
    allAverages = np.array([])
    for age in ["age_-18","age_18-24","age_25-34","age_35-44","age_45-49","age_50-55","age_56+"]:
        for job in ["movie_genre_Action","movie_genre_Adventure","movie_genre_Animation","movie_genre_Childrens","movie_genre_Comedy","movie_genre_Crime","movie_genre_Documentary","movie_genre_Drama","movie_genre_Fantasy","movie_genre_Film-Noir","movie_genre_Horror","movie_genre_Musical","movie_genre_Mystery","movie_genre_Romance","movie_genre_Sci-Fi","movie_genre_Thriller","movie_genre_War","movie_genre_Western"]:
            category=np.array(data[(data[age]==1) & (data[job]==1)])
            average=np.mean(category[:,-1])
            allAverages=np.append(allAverages,average)
    return allAverages
    

def bar_R_by_jobs_and_Age(data):
    test=averageByAgeAndjob(data)
    
    plt.figure()
    plt.bar(range(len(test)),test , 0.0001, color="y",align='center',hatch="x")
    
    plt.xlabel("$Jobs by AgeGroups$")
    plt.ylabel("$Average Rating$") #$$ change apearence of font
    plt.title("$Average Ratings By Jobs And AgeGroups$")
    
    plt.savefig("Average Ratings By Jobs And AgeGroups1.png") #to save the file
    
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for c, z in zip(['r', 'g', 'b', 'y'], [40,30,20,10,0]):
    
        start=len(test)*(z-10)/40
        end=len(test)*z/40
        
        ys = test[start:end]
        xs = np.arange(len(ys))
        # You can provide either a single color or an array. To demonstrate this,
        # the first bar of each set will be colored cyan.
        cs = [c] * len(xs)
        
        ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.2,edgecolor = "none")
        
    plt.title("$Average Ratings By Jobs And AgeGroups$")
    ax.set_xlabel('$Jobs by Age groups$')
    ax.set_zlabel('Ratings')
    
    plt.xticks([1],[""])
    plt.yticks([1],[""])
    plt.savefig("Average Ratings By Jobs And AgeGroups2.png") #to save the file

def error_Bar(data):
    under18 = np.array(data[data["age_-18"]==1])
    from18to24 = np.array(data[data["age_18-24"]==1])
    from25to34 = np.array(data[data["age_25-34"]==1])
    from35to44 = np.array(data[data["age_35-44"]==1])
    from45to49 = np.array(data[data["age_45-49"]==1])
    from50to55 = np.array(data[data["age_50-55"]==1])
    over56 = np.array(data[data["age_56+"]==1])

    avergaeUnder18=np.mean(under18[:,-1])
    avergaeFrom18to24 = np.mean(from18to24[:,-1])
    avergaeFrom25to34 = np.mean(from25to34[:,-1])
    avergaeFrom35to44 = np.mean(from35to44[:,-1])
    avergaeFrom45to49 = np.mean(from45to49[:,-1])
    avergaeFrom50to55 = np.mean(from50to55[:,-1])
    over56 = np.mean(over56[:,-1])
    averagesByAge=np.array([avergaeUnder18,avergaeFrom18to24,avergaeFrom25to34,avergaeFrom35to44,avergaeFrom45to49,avergaeFrom50to55,over56])
    #error bar values that vary with averageRating
    error = 0.1 + 0.2 * averagesByAge
    lower_error = 0.3 * error
    upper_error = error
    asymmetric_error = [lower_error, upper_error]
    fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
    ax0.errorbar([0,18,25, 35, 45, 50,55], averagesByAge, yerr=error, fmt='-o')
    ax0.set_title('$Average Ratings By Age Groups$, $Symmetric Error$')
    ax1.errorbar([0,18,25, 35, 45, 50,55], averagesByAge, xerr=asymmetric_error, fmt='o')
    ax1.set_title('$Average Ratings By Age Groups$, $Asymmetric Error$')
    ax1.set_yscale('log')
    plt.show()
    plt.savefig("Error Bar of Average Ratings By Age Groups.png") #to save the file



