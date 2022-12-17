use std::time;

enum OrderType { Buy, Sell }

struct Swap {
    /// Save an operation on wallet
    order_type: OrderType,
    amount: u128,
    price: u128,
    timestamp: u128,
}
impl Swap {
    fn new(order_type: OrderType, amount: u128, price: u128) -> Self {
        Self {
            order_type,
            amount,
            price,
            timestamp: time::SystemTime::now(),
        }
    }

    fn get_str_timestamp(&self) -> String {
        self.timestamp.format("%Y-%m-%d %H:%M:%S").to_string()
    }
}

struct Wallet {
    /// Wallet for trading
    balance: u128,
    swaps: Vec<Swap>,
}
impl Wallet{
    fn new(balance: u128) -> Self {
        Self {
            balance,
            swaps: Vec::new(),
        }
    }

    fn get_balance(&self) -> u128 {
        self.balance
    }

    fn get_swaps(&self) -> &Vec<Swap> {
        &self.swaps
    }
}

