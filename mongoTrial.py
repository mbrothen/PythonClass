# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:32:17 2020
Test out using a mongo db
@author: mbrothen
"""
import pymongo

def main():
    def petList():
        petList = [
            {"name": "Archie", "species": "cat", "age": 5},
            {"name": "Eleanor", "species": "cat", "age": 5},
            {"name": "Maddox", "species": "dog", "age": 8},
            {"name": "Chippy", "species": "ground squirrel", "age": None}
        ]
        return petList

    def myList():
        mylist = [
          {"_id": 1, "name": "John", "address": "Highway 37"},
          {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
          {"_id": 3, "name": "Amy", "address": "Apple st 652"},
          {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
          {"_id": 5, "name": "Michael", "address": "Valley 345"},
          {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
          {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
          {"_id": 8, "name": "Richard", "address": "Sky st 331"},
          {"_id": 9, "name": "Susan", "address": "One way 98"},
          {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
          {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
          {"_id": 12, "name": "William", "address": "Central st 954"},
          {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
          {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
          ]
        return mylist

    def createDatabase():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        customerDatabase = myclient["testDatbase"]
        # Create collection
        customerCollection = customerDatabase["customers"]
        return customerCollection

    def insertOne(db):
        dictionary = {"name": "Matt", "address": "Kenosha"}
        x = db.insert_one(dictionary)
        print("ID FIeld: " + str(x.inserted_id))

    def insertMultiple(db):
        x = db.insert_many(petList())
        print("Inserted IDs: " + str(x.inserted_ids))

    def insertMultipleSpecificIds(db):
        x = db.insert_many(myList())
        print("Inserted IDs: " + str(x.inserted_ids))

    def findOne(db):
        x = db.find_one()
        print("Find One: " + str(x))

    def findAll(db):
        print("Find All: ")
        for x in db.find():
            print(x)

    def findSome(db):
        print("Find Some: ")
        for x in db.find({}, {"_id": 0, "name": 1, "address": 1}):
            print(x)

    def loopPrint(results):
        # Aint nobody got time for that
        for x in results:
            print(x)

    def filterResults(db):
        # Only return results that match query
        print("Filtered Results: ")
        query = { "address": "Park Lane 38" }
        results = db.find(query)
        loopPrint(results)

    def advanceQuery(db):
        # us regex in query
        print("Advanced Query:")
        query = {"address": {"$gt": "S"}}
        results = db.find(query)
        loopPrint(results)

    def regExFilter(db):
        # us regex in query
        print("RegEx Query")
        query = {"address": {"$regex": "^S"}}
        results = db.find(query)
        loopPrint(results)

    def sort(db):
        # Apply sorting by column
        print("Sorted Results:")
        results = db.find().sort("name")
        loopPrint(results)

    def sortDescending(db):
        # reverse sort
        print("Descending Sort:")
        results = db.find().sort("name", -1)
        loopPrint(results)

    def deleteDocument(db):
        query = {"address": "Mountain 21"}
        db.delete_one(query)

    def deleteMany(db):
        query = {"address": {"$regex": "^S"}}
        x = db.delete_many(query)
        print(x.deleted_count, " documents deleted")

    def deleteAll(db):
        x = db.delete_many({})
        print(x.deleted_count, " documents deleted")

    def deleteCollection(db):
        db.drop()

    def update(db):
        print("Udpate:")
        query = {"address": "Valley 345"}
        newvalues = {"$set": {"address": "Canyon 123"}}
        db.update_one(query, newvalues)
        loopPrint(db.find())

    def updateMany(db):
        query = {"address": {"$regex": "^S"}}
        newvalues = {"$set": {"name": "Minnie"}}
        x = db.update_many(query, newvalues)
        print(x.modified_count, "documents updated.")

    def limit(db):
        print("Limit:")
        x = db.find().limit(5)
        loopPrint(x)

    collection = createDatabase()
    insertOne(collection)
    insertMultiple(collection)
    insertMultipleSpecificIds(collection)
    findOne(collection)
    findAll(collection)
    findSome(collection)
    filterResults(collection)
    advanceQuery(collection)
    regExFilter(collection)
    sort(collection)
    sortDescending(collection)
    update(collection)
    updateMany(collection)
    limit(collection)
    deleteDocument(collection)
    deleteMany(collection)
    deleteAll(collection)
    deleteCollection(collection)


main()
