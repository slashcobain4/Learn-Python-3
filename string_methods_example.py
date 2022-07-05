highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.

#First, start by printing highlighted_poems to the terminal and see how it displays.

print(highlighted_poems)

#The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.

#Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)

#Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.

#Start by creating a new empty list, highlighted_poems_stripped.

#Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  #poem not highlighted_poems_list, because we want to just look at each individual poem, not the entire list of poems

print(highlighted_poems_stripped)

#Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.

#Create a new empty list called highlighted_poems_details.

highlighted_poems_details = []

#Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

#Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.

#Create three new empty lists, titles, poets, and dates.

titles = []
poets = []
dates = []


#Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

#For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.

#review below
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])


#Finally, write a for loop that uses .format() to print out the following string for each poem:

#The poem TITLE was published by POET in DATE.

#run through python explainer to review

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))


