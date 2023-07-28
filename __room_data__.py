import random

from web.security.chaos_generator.triple_pendulum import encrypt_Text_New


def generate_Dummy_Room_Data(user_id: str, appliances_list: list):
    # all appliances_list
    loads = appliances_list

    data = []
    for a in loads:
        # cipher_load_type = encrypt_Text(str(a))
        cipher_load_type = str(a)
        # Generate random energy consumption per hour for a room
        v = random.randint(225, 235)
        f = random.randint(45, 55)
        pf = round(random.uniform(0.85, 0.95), 1)
        i = random.randint(1, 4)
        p = round(v * i * pf, 1)

        # encryption of values
        # cipher_v = encrypt_Text(str(v)); cipher_f = encrypt_Text(str(f))
        # cipher_pf = encrypt_Text(str(pf)); cipher_i = encrypt_Text(str(i))
        # cipher_p = encrypt_Text(str(p));

        cipher_v = encrypt_Text_New(str(v))
        cipher_f = encrypt_Text_New(str(f))
        cipher_pf = encrypt_Text_New(str(pf))
        cipher_i = encrypt_Text_New(str(i))
        cipher_p = encrypt_Text_New(str(p))

        data.append(
            {
                "load_type": cipher_load_type,
                "volt": cipher_v,
                "frequency": cipher_f,
                "power_factor": cipher_pf,
                "current": cipher_i,
                "power": cipher_p,
                "user_id": user_id,
            }
        )

    return data
