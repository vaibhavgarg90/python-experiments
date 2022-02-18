from bson import ObjectId

from service import mongo_service

obj_id = ""


def test_insert_data():
    global obj_id
    obj_id = str(mongo_service.insert_data({"a": 1}))
    print(obj_id)


def test_get_by_id():
    print(mongo_service.get_by_id(obj_id))


def test_list_data():
    print(list(mongo_service.list_data({"_id": ObjectId(obj_id)})))


def test_update_data():
    print(mongo_service.update_data({"_id": ObjectId(obj_id)}, {"a": 2}))


def test_delete_data():
    print(mongo_service.delete_data({"_id": ObjectId(obj_id)}))


if __name__ == "__main__":
    test_insert_data()
    test_get_by_id()
    test_list_data()
    test_update_data()
    test_get_by_id()
    test_delete_data()
