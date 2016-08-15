# Book recommendation model using Spark MLlib

Spark's documentation of Collaborative Filtering describes the steps involved in building a recommendation model. The following python here is based on the example provided there and performs the following operations
	1. Read data from Cassandra table as Spark RDD
	2. Build Recommendation model using Alternating least squares method
	3. Evaluate the model on training data
	4. Use MSE as a measure of accuracy of the Recommendation model.
