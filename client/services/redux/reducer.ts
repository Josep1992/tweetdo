import {combineReducers,Reducer} from "redux";
import {user as userReducer} from "./user";
import {todos as todosReducer} from "./todos";

export const rootReducer: Reducer = combineReducers({
    user: userReducer, 
    todos: todosReducer
});