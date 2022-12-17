use std::time;

pub enum OrderType { Buy, Sell }

pub struct Swap {
    /// Save an operation on wallet
    pub order_type: OrderType,
    pub amount: u128,
    pub price: u128,
    timestamp: u128,
}
impl Swap {
    pub fn new(order_type: OrderType, amount: u128, price: u128) -> Self {
        Self {
            order_type,
            amount,
            price,
            timestamp: time::SystemTime::now(),
        }
    }

    pub fn get_str_timestamp(&self) -> String {
        self.timestamp.format("%Y-%m-%d %H:%M:%S").to_string()
    }
}

pub struct Wallet {
    /// Wallet for trading
    balance: u128,
    swaps: Vec<Swap>,
}
impl Wallet{
    pub fn new(balance: u128) -> Self {
        Self {
            balance,
            swaps: Vec::new(),
        }
    }

    pub fn get_balance(&self) -> u128 {
        self.balance
    }

    pub fn get_swaps(&self) -> &Vec<Swap> {
        &self.swaps
    }
}

