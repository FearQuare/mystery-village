def create_citizen(id, identity, status, job="Unemployed"):
    """This function creates a citizen for our town"""
    created_citizen = {
        "id": id,
        "identity": identity,
        "job": job,
        "status": status,
    }

    return created_citizen