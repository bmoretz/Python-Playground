# Correlation Heat Map Utility (R)
#
# Input correlation matrix. Output heat map of correlation matrix.
# Requires R lattice package.
 
# Adapted from 
# Miller T. W. (2015) Modeling Techniques in Predictive Analytics with 
# Python and R: A Guide to Data Science, Upper Saddle River, N.J.: Pearson.
# Revised December 2016 by Thomas W. Miller

correlation_heat_map <- function(cormat, order_variable = NULL, title = "") {
    if (is.null(order_variable)) order_variable = rownames(cormat)[1]
    cormat_line <- cormat[order_variable, ]
    ordered_cormat <- 
        cormat[names(sort(cormat_line, decreasing=TRUE)),
            names(sort(cormat_line, decreasing=FALSE))]
    x <- rep(1:nrow(ordered_cormat), times=ncol(ordered_cormat))
    y <- NULL
    for (i in 1:ncol(ordered_cormat)) 
        y <- c(y,rep(i,times=nrow(ordered_cormat)))
    # use fixed format 0.XXX in cells of correlation matrix
    cortext <- sprintf("%0.3f", as.numeric(ordered_cormat))
    # two digits behind decimal point for large matrices
    if (nrow(ordered_cormat) >= 9) 
        cortext <- sprintf("%0.2f", as.numeric(ordered_cormat))    
    text.data.frame <- data.frame(x, y, cortext)
    text.data.frame$cortext <- as.character(text.data.frame$cortext)
    text.data.frame$cortext <- ifelse((text.data.frame$cortext == "1.000"),
        NA, text.data.frame$cortext)  # define diagonal cells as missing
    text.data.frame <- na.omit(text.data.frame)  # diagonal cells have no text
    # set magenta-to-cyan color palette  
    setcolor_palette <- colorRampPalette(c("#F8766D", "#FFFFFF", "#00BFC4"))    
    # use larger sized type for small matrices
    set_cex = 1.0
    if (nrow(ordered_cormat) <= 4) set_cex = 1.5  
    # smaller type for large matices
    if (nrow(ordered_cormat) >= 9) set_cex = 0.75    
    print(levelplot(ordered_cormat, cuts = 25, tick.number = 9,
        col.regions = setcolor_palette, 
        at = c(-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1,
        0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), 
        scales=list(tck = 0, x = list(rot=45), cex = set_cex),
        xlab = "", 
        ylab = "",
        main = title,
        panel = function(...) {
            panel.levelplot(...)  
            panel.text(text.data.frame$x, text.data.frame$y, 
            labels = text.data.frame$cortext, cex = set_cex)
            }))
    }
  
  
  
