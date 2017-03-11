all: client server

client:
	@echo "--> Generating Python client files"
	python3 -m grpc_tools.protoc -I protobuf/ --python_out=. --grpc_python_out=. protobuf/primefactor.proto
	@echo ""

server:
	@echo "--> Generating Go files"
	protoc -I protobuf/ --go_out=plugins=grpc:protobuf/ protobuf/primefactor.proto
	@echo ""

install:
	@echo "--> Installing Python grpcio tools"
	pip3 install -U grpcio grpcio-tools
	@echo ""
