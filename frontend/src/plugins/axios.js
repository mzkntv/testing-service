import axios from 'axios';

document.cookie = 'csrftoken=1ZSUesZthsUvpZk2UZRT75mzUsX0ZCxWlNe18LWQWuJWknNHcYZ6dJBnENveu71L; sessionid=r72afita5rzyjg2tr6veox3tf49jor90'

export const HTTP = axios.create({
  baseURL: `http://127.0.0.1:5173/`,
  withCredentials: true,
  headers: {
    'X-CSRFToken': '1ZSUesZthsUvpZk2UZRT75mzUsX0ZCxWlNe18LWQWuJWknNHcYZ6dJBnENveu71L',
  }
})
