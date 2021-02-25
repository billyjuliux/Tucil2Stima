# deklarasi kelas elemen graf
# graf akan didefinisikan sebagai array of elemen graf
class graph_elmt :
    def __init__(self,name,indeg,next_courses) :
        self.name = name
        self.indeg = indeg
        self.next_courses = next_courses

# prosedur membaca input file dan mengubahnya menjadi array of pasangan course dan prerequisites nya
def readFile(fileName) :
    f = open(fileName,"r")
    read_out = f.readlines()

    course_prereq = []
    for line in read_out :
        course_prereq.append(line.replace('\n','').replace('.','').split(", "))

    return course_prereq

# fungsi mencari indeks diberikan nama mata kuliah pada suatu graphList
# name dipastikan ada
def searchName(graphList,name) :
    i = 0
    while(graphList[i].name != name) :
        i += 1
    return i

# prosedur untuk membuat graf dari array of pasangan course dan prerequisitenya
def makeGraph(course_prereq) :
    # bagi menjadi array of course dan array of prerequisite
    names = []
    prereqs = []
    for course in course_prereq :
        names.append(course[0])
        curr_prereqs = []
        for i in range(len(course)-1) :
            curr_prereqs.append(course[i+1])
        prereqs.append(curr_prereqs)

    # secara sederhana, akan dilakukan "inverse", sehingga tiap elemen dari graf akan mencatat course lanjutannya, bukan prerequisite nya
    graphList = []
    for name in names :
        curr_elmt = graph_elmt(name,0,[])
        graphList.append(curr_elmt)

    courseNum = 0
    for prereq in prereqs :
        for name in prereq :
            # tambahkan mata kuliah yang merupakan lanjutan
            graphIdx = searchName(graphList,name)
            graphList[graphIdx].next_courses.append(graphList[courseNum].name)

            # tambahkan in degree dari mata kuliah lanjutan
            graphList[courseNum].indeg += 1
        courseNum += 1

    return graphList

# fungsi mengecek apakah in degree dari tiap graph sudah 0
# true jika semua in degree 0
# false jika ada mata kuliah dengan in degree > 0
def allPrinted(graphList):
    for elmt in graphList :
        if elmt.indeg >= 0 :
            return False
    return True

# fungsi mengembalikan list nama mata kuliah yang memiliki in degree 0
def zeroIndeg(graphList) :
    result = []
    for elmt in graphList :
        if elmt.indeg == 0 :
            result.append(elmt.name)
    return result

# main program
def main() :
    graphList = makeGraph(readFile("input.txt"))

    if (graphList != []) :
        semesterCounter = 0
        while (not allPrinted(graphList)) :
            print("Semester " + str(semesterCounter+1) + " : ", end="")
            printables = zeroIndeg(graphList)
            # print mata kuliah dengan in degree 0
            for to_print in printables :
                print(to_print, end="")
                if (to_print != printables[len(printables)-1]) :
                    print(", ", end="")
                else :
                    print()

                # di next courses nya, in degree dikurangi 1
                graphIdx = searchName(graphList,to_print)
                curr_next_courses = graphList[graphIdx].next_courses
                for name in curr_next_courses :
                    next_graphIdx = searchName(graphList,name)
                    graphList[next_graphIdx].indeg -= 1

                # agar tidak di print lagi, yg sudah 0 dibuat jadi -1
                graphList[graphIdx].indeg = -1
            
            semesterCounter += 1
    else :
        print("Tidak ada data yang valid!")
        

main()