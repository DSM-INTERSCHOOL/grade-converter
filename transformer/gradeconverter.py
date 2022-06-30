import pandas as pd



def orderList(s):
    elements = s.split(',')
    elements.sort()      
    return ("".join(elements))


def to_grade_card(grades):
    df_original = pd.read_json(grades)
    tr_bulletin = pd.pivot_table(df_original,index=["idTeacher", "teacherName","idAcademicYear","academicYear","idAcademicStage","academicStage","idAcademicProgram","academicProgram","idAcademicMode","academicMode","idSchoolYear","schoolYear","idGroup","group","idFaculty","faculty","idAcademy","academy","idDepartment","department","idCategory","category","idPerson","personName","idCourse","courseName","position","ordering"],values=["mark","absence","behaviour","note","extra1","extra2","extra3"],columns=["idTerm"],aggfunc="first")
    tr_bulletin = tr_bulletin.sort_values(["idGroup","personName", "position","ordering"], ascending = (True, True, True,True))
    
    print("MATERIA GENERAL")
    #print(tr_bulletin)
    #tr_bulletin_copy = tr_bulletin[:]
    #tr_bulletin_copy.reset_index()
    #tr_bulletin_copy.to_csv("general_bolletin.csv")
    tr_bulletin.columns= ["_".join((i,str(j))) for i,j in tr_bulletin.columns]  
    tr_bulletin.reset_index(inplace=True)
    #tr_bulletin.columns= tr_bulletin.index.names + ["_".join((i,str(j))) for i,j in tr_bulletin.columns]    
      
    
    #print(tr_bulletin.index.names)
    
    print("CARD")
    print(tr_bulletin)
    #print(tr_bulletin.iloc[:2,:2])
    return tr_bulletin.to_json(orient="records") 