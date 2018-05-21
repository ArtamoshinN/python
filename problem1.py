
def read_input():
    servers_num = int(input())
    servers = []
    errors = []
    for i in range(servers_num):
        server_prob, error_prob = [int(i) for i in input().split()]
        servers.append(server_prob)
        errors.append(error_prob)

    return servers_num, servers, errors


def main():
    servers_num, servers, errors = read_input()
    error_parts = [servers[i] * errors[i] for i in range(servers_num)]
    sum_errors = sum(error_parts)
    results = [error_parts[i] / sum_errors for i in range(servers_num)]

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
