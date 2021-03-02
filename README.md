# astros_cheating

<<<<<<< HEAD
# <div align="center"> Astros Cheating Scandal - A "Statistical" Advantage </div>
## <div align="center"> Did the Astros gain a statistical advantage during the 2016 cheating scandal? </div>

## Introduction
Nearly, three years ago the Astros became World Champions for the first time in team history.

For myself and millions of other Houstonians, it was the greatest sports moment for our city since the “Dream Team”.

In 2019, the internet helped reveal the Astros were illegally stealing signs using the aid of a camera placed in the outfield of their home field, Minute Maid Park.
<hr>

## Motivation and Question
The Astros won game 7 of the 2017 World Series IN Los Angeles.

The Astros didn’t win every game at HOME and didn’t lose every AWAY game.

Did the Astros gain a statistical advantage by using technology to illegally* steal signs during home games in the 2017 season?

*sign stealing is considered standard and acceptable practice in baseball. For instance, if a runner is at second, they are allowed to attempt to steal signs from his vantage point. Also, pitchers stealing signs from bullpen (typically located behind the outfield) is standard practice. 


<hr>

## Data

I compared the batting statistics of home games in 2017 other seasons where cheating did not occur. 

For sample data, I scraped the batting statistics of game logs from BaseballReference.com for every team for the 2016-2019 seasons using the Python libraries Requests, BeautifulSoup, and Selenium.

These tables were analyzed in a Jupyter notebook using the Python libraries Pandas, Matplotlib, and Scipy.

<hr>

## Results
![Google slides](https://docs.google.com/presentation/d/1gSG-Mp-hF2VJSk-AV4ZL5yBG-SuRmoIIbvnsa0fxA-4/edit#slide=id.g742e3e7cd_1_33)

### All books (n=8,800)

A scatter plot of average rating of each book against its score does not show any discernible difference in the mean of the ratings as score increases.


The histogram of the ratings show that they are normally distributed.
* Mean = 4.071
* Standard Deviation = 0.379

![Fig 2. Histogram of overall ratings](img/all_ratings_histogram.png)

When the ovearll data set is split by quality, ratings for both groups of books are normally distributed.
* Low Quality Books
    * Mean = 4.072
    * Standard Deviation = 0.454
* High Quality Books
    * Mean = 4.069
    * Standard Deviation: 0.286

![Fig 3. Histogram of overall ratings by quality](img/all_ratings_by_rank_histogram.png)

We can see that the mean rating score for the lower quality books is actually slightly higher than the mean rating score for the higher quality books. This is likely largely due to the higher number of 5-star rated books, visible in the plot of low quality books.

A Welch's t-test indicates there is no statistical difference between the ratings of the low and high quality books.

* Hypotheses
    * Null: Mean Low Quality Rating = Mean High Quality Rating
    * Alternative: Mean Low Quality Rating ≠ Mean High Quality Rating

* Results
    * t = 0.370
    * p = 0.711

### Books with at least 2 votes and at least 10 ratings (condensed)

A look at the scatter plots of the average rating of each book against its score for the "condensed" set of books looks very similar to the scatter plot for all books. Once again, the averege rating of almost every book is above 3, and the mean rating does not appear to change, regardless of its score.

![Fig 4. Scatter Plot of Rating vs Score for Condensed Set](img/sufficient_scatter_rating_score.png)

The histogram of the ratings for the condensed set shows they are also normally distributed.

* Mean = 4.060
* Standard Deviation = 0.280

![Fig 5. Histogram of condensed data ratings](img/sufficient_ratings_histogram.png)

When the condensed data set is divided into low and high quality, the ratings for both groups of books are again normally distributed. Also noticeable in this set, the number of 5-star rated books is clearly more comparable between the 2 groups, and the mean rating for the higher quality books is now higher than the mean rating for the lower quality books.

* Low Quality Books
    * Mean = 4.054
    * Standard Deviation = 0.285
* High Quality Books
    * Mean = 4.066
    * Standard Deviation: 0.275

![Fig 6. Histogram of condensed data ratings by rank](img/sufficient_ratings_by_rank_histogram.png)

The Welch's t-test on this data set also indicates that though the p-value is much smaller, there is still not sufficient evidence that there is a difference between the ratings of the low and high quality books.

* Hypotheses
    * Null: Mean Low Quality Rating = Mean High Quality Rating
    * Alternative: Mean Low Quality Rating ≠ Mean High Quality Rating

* Results
    * t = -1.712
    * p = 0.087

![Fig 7. Ttest distribution](img/2_sided_ttest_distribution.png)

<hr>

## Conclusions

I was not able to find evidence that there is a difference in the average ratings of higher quality books and lower quality books on Goodreads. This means I can't trust the ratings (or at least not only the ratings) when determining the quality of a book.

<hr>

## Further Research

I would love to dive farther into how readers rate books on Goodreads. There many ideas and theories I would to test.
* If I broke up the groups of books into smaller tiers, would I see a differece then? In other words, maybe I would be able to see a pattern emerge if I looked at the top 100 books vs. other groups of 100.
* Is length of book associated with rating? I suspect there may be a sweet spot for length where readers feel there is a solid story without it dragging on too long.
* Is publication year associated with rating? Do people rate older "classics" higher? Are they more exicted about new books?

<hr>

## Final Word

I have read 21 of the top 100 books on the list, with two more currently waiting on my bookshelf. How many have you read? Follow the link below and count them up!

=======
[Google slides](https://docs.google.com/presentation/d/1gSG-Mp-hF2VJSk-AV4ZL5yBG-SuRmoIIbvnsa0fxA-4/edit?usp=sharing)
>>>>>>> a7ab7e3604f7d0efa11184855d137a7ddad54a07
