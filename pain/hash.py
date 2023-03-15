import hmac

# Open database file
with open('my_database.db', 'rb') as f:
    # Read file contents
    file_contents = f.read()

    # Hash the file contents using a secret key
    secret_key = b'my_secret_key'
    hashed_contents = hmac.new(secret_key, file_contents).digest()

    # Write the hashed contents to a new file
    with open('my_database_hash.txt', 'wb') as hash_file:
        hash_file.write(hashed_contents)
