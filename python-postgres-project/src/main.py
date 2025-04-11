import docker

def create_postgres_container():
    client = docker.from_env()
    
    try:
        # Pull the PostgreSQL image
        client.images.pull('postgres:latest')
        
        # Create and start the PostgreSQL container
        container = client.containers.run(
            'postgres:latest',
            environment={
                'POSTGRES_USER': 'user',
                'POSTGRES_PASSWORD': 'password',
                'POSTGRES_DB': 'mydatabase'
            },
            ports={'5432/tcp': 5432},
            volumes={'postgres_data': {'bind': '/var/lib/postgresql/data', 'mode': 'rw'}},
            detach=True
        )
        
        print(f'PostgreSQL container started with ID: {container.id}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    create_postgres_container()