@echo off
mkdir result
ECHO "<<<<<<<<<<<<<<<<<<<<< Rating Counter <<<<<<<<<<<<<<<<<<<<<"
python RatingCounter.py data/u.data > result/rating_counter_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Friends by age <<<<<<<<<<<<<<<<<<<<<"
python friends_by_age.py data/fakefriends.csv > result/friends_by_age_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Min Temperatures <<<<<<<<<<<<<<<<<<<<<"
python MinTemperatures.py data/1800.csv > result/min_temperature_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Max Temperatures <<<<<<<<<<<<<<<<<<<<<"
python MaxTemperatures.py data/1800.csv > result/max_temperature_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Word frequency <<<<<<<<<<<<<<<<<<<<<"
python word_frequency.py data/book.txt > result/word_frequency_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Word frequency counter <<<<<<<<<<<<<<<<<<<<<"
python word_frequency_counter.py data/book.txt > result/word_frequency_counter_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Spend by customer sorted <<<<<<<<<<<<<<<<<<<<<"
python spend_by_customer_sorted.py data/customer-orders.csv > result/spend_by_customer_sorted_result.txt

ECHO "<<<<<<<<<<<<<<<<<<<<< Word frequency with combiner <<<<<<<<<<<<<<<<<<<<<"
python word_frequency_with_combiner.py data/book.txt > result/word_frequency_with_combiner_result.txt
