import {createStore, applyMiddleware,Store} from "redux";
import thunkMiddleware from "redux-thunk";
import {rootReducer} from "./reducer";
import {composeWithDevTools} from "redux-devtools-extension";


export function configureStore():Store {
    const middleWareEnhancer = applyMiddleware(thunkMiddleware);
    return createStore(rootReducer, composeWithDevTools(middleWareEnhancer));
}