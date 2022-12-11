import axios, * as others from 'axios';
import {USER_STATISTIC_URL} from '../utils/consts';


export default class ApiCalls{

    callGetUserStatistic= (id) => {
        return axios.get(USER_STATISTIC_URL + `${id}`)
    }
}

