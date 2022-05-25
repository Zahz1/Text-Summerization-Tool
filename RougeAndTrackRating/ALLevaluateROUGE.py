import rouge, os, math

#configuring Rouge eveluation
evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l', 'rouge-w'],
                       max_n=2,
                       limit_length=True,
                       length_limit=100,
                       length_limit_type='words',
                       alpha=0.5, # Default F1_score
                       weight_factor=1.2,
                       stemming=True)


article_dir_Main = "Articles"
article_Lists = os.listdir(article_dir_Main)

#print avalible files
for index in range(0,len(article_Lists)):
    print(str(index) + ": " + article_Lists[index] + '\n')

#get user input for what article to get Rouge data for (add in error check)
#article_FileName = article_Lists[int(input("Enter Article Index: "))]

for article_FileName in article_Lists:

    # setting up data path
    article_dir = os.path.join(article_dir_Main, article_FileName)
    references_dir = article_dir + "/reference_sum"
    system_dir = article_dir + "/system_sum"

    #organize system and referemce summaries into two different lists (saving fileNames)
    curr_ref_dir = references_dir
    curr_sys_dir = system_dir

    #organize referemce summaries
    ref_names = []
    ref_summaries = []
    for filename in os.listdir(curr_ref_dir):
        #print(filename)
        f = os.path.join(curr_ref_dir, filename)
        if os.path.isfile(f):
            file = open(f, "r")
            ref_names.append(filename)
            sum = file.read().replace("\n", " ")
            ref_summaries.append(sum)

    #organize system summaries
    sys_names = []
    sys_summaries = []
    for filename in os.listdir(curr_sys_dir):
        #print(filename)
        f = os.path.join(curr_sys_dir, filename)
        if os.path.isfile(f):
            file = open(f, "r")
            sys_names.append(filename)
            sum = file.read().replace("\n", " ")
            sys_summaries.append(sum)



    #openFile to store results
    #metrics_list = ['rouge-1']
    Scores = [[]]

    fixedFile = open(("Results/results_" + article_FileName +".csv"), "w")
    fixedFile.write(article_FileName + "\n")
    fixedFile.close()

    fixedFile = open(("Results/results_" + article_FileName +".csv"), "a")

    #fixedFile.write(article_FileName + "\n")

    fixedFile.write(" ,")
    for sum in sys_names:
        sizeS = len(sum)
        fixedFile.write(sum[0:sizeS-4] + ",")

    fixedFile.write("\n")

    for i in range(0, len(ref_summaries)):

        sizeR = len(ref_names[i])
        fixedFile.write((ref_names[i][0:sizeR-4]) + "\n")

        Scores = [[],[],[],[],[],[],[],[],[],[]] #set this up with a for loop

        for j in range(0, len(sys_summaries)):
            #fixedFile.write(sys_names[j] + " + " + ref_names[i] + "\n")

            scores = evaluator.get_scores(sys_summaries[j], ref_summaries[i])

            for metric, results in sorted(scores.items(), key=lambda x: x[0]):
                #fixedFile.write(metric + "," + str(results.get('f')) + "\n")
                Scores[j].append(results.get('f'))

        #for metricsNUM in range(0,len(metrics_list)):
            #print(metrics_list[0])
        fixedFile.write('rouge-1' + ",")
        for scores in Scores:
            print(article_FileName)
            #print(scores)
            print(scores)
            if (len(scores) != 0):
                fixedFile.write(str(float(math.trunc(scores[0]*1000))/float(1000)) + ",")

        fixedFile.write("\n")


print("Program finished. F-Scores stored in Results.csv")
