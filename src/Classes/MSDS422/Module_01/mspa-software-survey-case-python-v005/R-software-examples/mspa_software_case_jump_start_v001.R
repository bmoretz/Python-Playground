# Jump-Start Example: R analysis of MSPA Software Survey

# shows how to read in data from a comma-delimited text file
# manipuate data, create new count variables, define factor variables,
# work with a hash table for recoding data 

# visualizations in this program are routed to external pdf files
# so they may be included in printed or electronic reports

# external libraries for visualizations and data manipulation
# ensure that these have been installed prior to calls
library(lattice) 
library(ggplot2)

# set up hash fuctions similar to Python dictionary data structure
library(hash)  

# user-defined function useful for data visualization
# helps with review of correlation matrices
source("code_correlation_heat_map.R")

# set color constants for visualizations
HEX_BLUE <- "#3953A4"  
HEX_GREEN <- "#13A049" 
HEX_RED <- "#EE3166"  
HEX_WHITE <- "#FFFFFF"  
HEX_GREY <- "#C2C2D6"  
HEX_BLACK <- "#000000"

# read in comma-delimited text file
# note that IPAddress is formatted as an actual IP address
# but is actually a random-hash of the original IP address
valid_survey_input <- 
    read.csv(file = "mspa_survey_data.csv", 
    stringsAsFactors = FALSE)
    
cat("\nNumber of Respondents =", nrow(valid_survey_input))
        
cormat <- cor(valid_survey_input[, 2:16])
short_var_names <- c("My_Java", "My_JavaSript", "My_Python", "My_R", "My_SAS",
    "Prof_Java", "Prof_JavaSript", "Prof_Python", "Prof_R", "Prof_SAS",
    "Ind_Java", "Ind_JavaSript", "Ind_Python", "Ind_R", "Ind_SAS")
rownames(cormat) <- short_var_names
colnames(cormat) <- short_var_names

# examine intercorrelations among software preference variables
pdf(file = "fig_cor_heat_map_language_prefernces_complete.pdf", 
    width = 7.5, height = 7.5, paper = "letter")
correlation_heat_map(cormat, order_variable = NULL, 
   title = "Correlations for Original Computer Language Items")
dev.off()

# define new variables for working data frame
# language preferences computed as averages 
# for one individual at a time
Java <- JavaScript <- Python <- R <- SAS <- numeric(nrow(valid_survey_input))

for (i in seq(along = valid_survey_input$Personal_JavaScalaSpark)) {
    Java[i] <- mean(valid_survey_input$Personal_JavaScalaSpark[i],
        valid_survey_input$Professional_JavaScalaSpark[i], valid_survey_input$Industry_JavaScalaSpark[i])
    JavaScript[i] <- mean(valid_survey_input$Personal_JavaScriptHTMLCSS[i],
        valid_survey_input$Professional_JavaScriptHTMLCSS[i], valid_survey_input$Industry_JavaScriptHTMLCSS[i])   
    Python[i] <- mean(valid_survey_input$Personal_Python[i],
        valid_survey_input$Professional_Python[i], valid_survey_input$Industry_Python[i])     
    R[i] <- mean(valid_survey_input$Personal_R[i],
        valid_survey_input$Professional_R[i], valid_survey_input$Industry_R[i])     
    SAS[i] <- mean(valid_survey_input$Personal_SAS[i],
        valid_survey_input$Professional_SAS[i], valid_survey_input$Industry_SAS[i])       
    } # end of for-loop for creating preference variables    

# create new data frame with the summary language variables    
working_survey_input <- data.frame(Java, JavaScript, Python, R, SAS)  

# add Courses_Completed to the working data frame
working_survey_input$Courses_Completed <- 
    valid_survey_input$Courses_Completed

# let nonresponse on sliders be zero interest
# and create interest variables for use in the new data frame
working_survey_input$Python_Course_Interest <- 
    ifelse(is.na(valid_survey_input$Python_Course_Interest), 0,
        valid_survey_input$Python_Course_Interest) 
        
working_survey_input$Foundations_DE_Course_Interest <- 
    ifelse(is.na(valid_survey_input$Foundations_DE_Course_Interest), 0,
        valid_survey_input$Foundations_DE_Course_Interest) 
        
working_survey_input$Analytics_App_Course_Interest <- 
    ifelse(is.na(valid_survey_input$Analytics_App_Course_Interest), 0,
        valid_survey_input$Analytics_App_Course_Interest)         
        
working_survey_input$Systems_Analysis_Course_Interest <- 
    ifelse(is.na(valid_survey_input$Systems_Analysis_Course_Interest), 0,
        valid_survey_input$Systems_Analysis_Course_Interest)  
        
# software count variables to add to the data frame
working_survey_input$Python_Courses <- numeric(nrow(working_survey_input))
working_survey_input$R_Courses <- numeric(nrow(working_survey_input))
working_survey_input$SAS_Courses <- numeric(nrow(working_survey_input))
for (istudent in seq(along = working_survey_input$Python_Courses)) {

    if (valid_survey_input$PREDICT400[istudent] != "")
        working_survey_input$Python_Courses[istudent] <-
            working_survey_input$Python_Courses[istudent] + 1
    if (valid_survey_input$PREDICT420[istudent] != "")
        working_survey_input$Python_Courses[istudent] <-
            working_survey_input$Python_Courses[istudent] + 1
    if (valid_survey_input$PREDICT452[istudent] != "")
        working_survey_input$Python_Courses[istudent] <-
            working_survey_input$Python_Courses[istudent] + 1
    if (valid_survey_input$PREDICT453[istudent] != "")
        working_survey_input$Python_Courses[istudent] <-
            working_survey_input$Python_Courses[istudent] + 1
            
    if (valid_survey_input$PREDICT401[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1
    if (valid_survey_input$PREDICT413[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1
    if (valid_survey_input$PREDICT450[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1        
    if (valid_survey_input$PREDICT451[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1        
    if (valid_survey_input$PREDICT454[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1        
    if (valid_survey_input$PREDICT455[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1        
    if (valid_survey_input$PREDICT456[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1        
    if (valid_survey_input$PREDICT457[istudent] != "")
        working_survey_input$R_Courses[istudent] <-
            working_survey_input$R_Courses[istudent] + 1 

    if (valid_survey_input$PREDICT410[istudent] != "")
        working_survey_input$SAS_Courses[istudent] <-
            working_survey_input$SAS_Courses[istudent] + 1
    if (valid_survey_input$PREDICT411[istudent] != "")
        working_survey_input$SAS_Courses[istudent] <-
            working_survey_input$SAS_Courses[istudent] + 1

    }        

# work with user-defined function to make bar chart
# make pretty ggplot2 bar chart for number of SAS courses taken
pdf(file = "fig_ggplot2_bar_chart_for_number_sas_courses.pdf", 
    width = 7.5, height = 7.5, paper = "letter")  
ggplot_object <- ggplot(data = working_survey_input,
    aes(x = SAS_Courses)) +
geom_bar(fill = HEX_BLUE, colour = HEX_BLUE) +
ggtitle("Bar Chart for Number of SAS Courses Taken\n") +
xlab("\nNumber of SAS Courses Taken") +
ylab("Number of Students") 
print(ggplot_object)
dev.off()


# hash table for computing terms to graduate from graduation dates
# works like an Excel lookup table, Perl hash, or Python dictionary
mykeys <- c("Fall 2016", "Winter 2017", "Spring 2017", "Summer 2017",
    "Fall 2017", "Winter 2018", "Spring 2018", "Summer 2018", "Fall 2018",
    "Winter 2019", "Spring 2019", "Summer 2019", "Fall 2019",  "Winter 2017",
    "2020 or Later")
myvalues <- 0:(length(mykeys) - 1)
# create the hash table object (similar to dictionary in python)
mydate_dict <- hash(keys = mykeys, values = myvalues)

working_survey_input$Graduate_Date <- valid_survey_input$Graduate_Date

working_survey_input$Terms_to_Graduate <- numeric(nrow(working_survey_input))

# determine the new values for number of terms to graduation by hash
for (item in seq(along = working_survey_input$Graduate_Date)) {
    if (working_survey_input$Graduate_Date[item] == "")
        working_survey_input$Terms_to_Graduate[item] <- NA

    if (working_survey_input$Graduate_Date[item] != "")
        working_survey_input$Terms_to_Graduate[item] <-
            values(mydate_dict, keys = working_survey_input$Graduate_Date[item])   
    }

# examine the structure of the working_survey_data so far
print(str(working_survey_input))

# use R standard graphics to make a scatter plot
# jittered with open-circle points to avoid overplotting issue
pdf(file = "fig_plot_simple_scatter_plot.pdf", 
    width = 7.5, height = 7.5, paper = "letter")
with(working_survey_input, 
    plot(jitter(Courses_Completed), jitter(Terms_to_Graduate), 
        las = 1,
        xlab = "Number of Coures Completed",
        ylab = "Expected Number of Terms Before Graduation"))
dev.off()    

# use R lattice package to create histogram for groups defined by
# the number of SAS courses taken

# it is often useful to set up a data frame just for plotting
plotting_data_frame <- 
    working_survey_input[, c("Terms_to_Graduate", "SAS_Courses")]
plotting_data_frame$SAS_Courses <- 
    factor(plotting_data_frame$SAS_Courses,
        levels = c(0, 1, 2), 
        labels = c("No SAS Courses", "PREDICT 410 Only", "PREDICT 410/411"))
    
# set up function for lattice panels for up to five groups
# use special colors for the panel rectangles and text for group labels
myStripRectColorsGrey <- c(HEX_GREY, HEX_GREY, HEX_GREY, HEX_GREY, HEX_GREY)
myStripTextColorsBlack <- c(HEX_BLACK, HEX_BLACK, HEX_BLACK, HEX_BLACK, HEX_GREY)

myStripStyleGreyBlack <- function(which.panel, factor.levels, ...) {
    panel.rect(0, 0, 1, 1, border = 1, 
        col = myStripRectColorsGrey[which.panel])
    panel.text(x = 0.5, y = 0.5, 
        col = myStripTextColorsBlack[which.panel],
        lab = paste(factor.levels[which.panel]))
    }

pdf(file = "fig_lattice_terms_to_graduate_by_sas_courses.pdf", 
    width = 7.5, height = 8, paper = "letter")
lattice_plot_object <- histogram(~Terms_to_Graduate | SAS_Courses, 
    data = plotting_data_frame,             
    strip = myStripStyleGreyBlack,
    col = "darkblue", border = "lightgrey",
    type = "percent", xlab = "Expected Number of Terms Before Graduation",
    ylab = "Percentage of Students in Group",
    breaks = 0:14,
    layout = c(1,3),
    main = "Expected Number of Terms Before Graduation for SAS Groups")
print(lattice_plot_object)  
dev.off()

































