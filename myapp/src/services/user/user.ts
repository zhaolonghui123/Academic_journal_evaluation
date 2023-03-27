import axios from "axios"
import { userURL } from "../url"

export async function  getAllUser() {
    return await axios.get(userURL.getAllUser)
}