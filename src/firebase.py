import requests
import grpc
import protos

def create_account(username, password):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = protos.user_pb2_grpc.UserStub(channel)
        request = protos.user_pb2.SignInSignUpRequest(email=username, password=password)
        response = stub.SignUp(request)
        print(response.message)
