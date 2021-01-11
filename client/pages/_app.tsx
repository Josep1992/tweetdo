import * as React from "react";
import '../styles/globals.scss'
import { AppProps } from "next/app";
import { ChakraProvider } from "@chakra-ui/react"
import { configureStore } from "../services/redux/store";
import { Provider } from "react-redux";
import { Store } from "redux";

const store:Store = configureStore();

const App: React.FunctionComponent<AppProps> = ({ Component, pageProps }: AppProps): React.ReactElement => {
  return (
    <Provider store={store}>
      <ChakraProvider>
        <Component {...pageProps} />
      </ChakraProvider>
    </Provider>
  );
}

export default App;
