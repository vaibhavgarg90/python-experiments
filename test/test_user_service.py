from bson import ObjectId

from service import user_service

obj_id = ""


def test_insert_data():
    global obj_id
    obj_id = str(user_service.insert_user({"a": 1}))
    print(obj_id)


def test_get_by_id():
    print(user_service.get_user_by_id(obj_id))


def test_list_data():
    print(list(user_service.list_users({"_id": ObjectId(obj_id)})))


def test_update_data():
    print(user_service.update_user({"_id": ObjectId(obj_id)}, {"a": 2}))


def test_delete_data():
    print(user_service.delete_user({"_id": ObjectId(obj_id)}))


if __name__ == "__main__":
    test_insert_data()
    test_get_by_id()
    test_list_data()
    test_update_data()
    test_get_by_id()
    test_delete_data()
